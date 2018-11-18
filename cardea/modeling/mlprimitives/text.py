import re

import pandas as pd

import langdetect
from iso639 import NonExistentLanguageError, to_name
from nltk.corpus import stopwords


class TextCleaner(object):
    RE_NON_ALPHA = re.compile('[^a-z]+')

    RE_SYMBOLS = re.compile('[-]')

    RE_NON_ALNUM = re.compile('[^\w\d]')

    RE_ACCENTS = {
        'a': re.compile('[àâáäåã]'),
        'e': re.compile('[èêéë]'),
        'i': re.compile('[ìîíï]'),
        'o': re.compile('[òôóö]'),
        'u': re.compile('[ùûúü]')
    }

    STOPWORDS = dict()

    def __init__(self, column=None, language='multi', lower=True, accents=True,
                 stopwrods=True, non_alpha=True, single_chars=True):
        self.column = column
        self.language = language
        self.language_code = None

        self.lower = lower
        self.accents = accents
        self.stopwords = stopwords
        self.non_alpha = non_alpha
        self.single_chars = single_chars

    @staticmethod
    def detect_language(texts):
        texts = pd.Series(texts)
        language_codes = texts.apply(langdetect.detect).value_counts()
        return language_codes.index[0]

    def fit(self, X):
        if self.language == 'auto':
            if self.column:
                texts = X[self.column]
            else:
                texts = pd.Series(texts)

            self.language_code = self.detect_language(texts)

        elif self.language != 'multi':
            self.language_code = self.language

    @classmethod
    def _clean_accents(cls, text):
        for sub, regex in cls.RE_ACCENTS.items():
            text = regex.sub(sub, text)

        return text

    @classmethod
    def get_stopwords(cls, language_code):
        if language_code in cls.STOPWORDS:
            return cls.STOPWORDS[language_code]

        try:
            names = [l.strip().lower() for l in to_name(language_code).split(';')]
        except NonExistentLanguageError:
            return []

        for name in names:
            try:
                sw = stopwords.words(name)
                cls.STOPWORDS[language_code] = sw
                return sw

            except Exception:
                pass

        return []

    def _remove_stopwords(self, text):
        if self.language_code:
            language_code = self.language_code

        elif self.language == 'multi':
            language_code = langdetect.detect(text)

        sw = self.get_stopwords(language_code)

        return ' '.join(word for word in text.split() if word not in sw)

    @classmethod
    def _remove_non_alpha(cls, text):
        text = cls.RE_SYMBOLS.sub('', text)
        text = cls.RE_NON_ALPHA.sub(' ', text)
        return ' '.join(text.split())

    @classmethod
    def _remove_single_chars(cls, text):
        words = text.split()
        return ' '.join(word for word in words if len(word) > 1)

    def produce(self, X):
        if self.column:
            texts = X[self.column]
        else:
            texts = pd.Series(X)

        texts = texts.fillna('')

        if self.lower:
            texts = texts.str.lower()

        if self.accents:
            texts = texts.apply(self._clean_accents)

        if self.stopwords:
            texts = texts.apply(self._remove_stopwords)

        if self.non_alpha:
            texts = texts.apply(self._remove_non_alpha)

        if self.single_chars:
            texts = texts.apply(self._remove_single_chars)

        if self.column:
            X[self.column] = texts
            return X

        else:
            return texts
