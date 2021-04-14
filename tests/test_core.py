import os

import pandas as pd
from sklearn.datasets import load_iris

from cardea.core import Cardea
from cardea.data import download


def prediction_problem_function(es):
    def label(ds):
        return False

    meta = {
        "entity": "Appointment",
        "target_entity": "identifier",
        "time_index": "created",
        "type": "classification",
        "num_examples_per_instance": 1
    }

    df = es['Appointment'].df.iloc[:100]

    return label, df, meta


class TestCardea:

    @classmethod
    def setup_class(cls):
        cls.X, cls.y = load_iris(return_X_y=True)

    def setup(self):
        data_path = download('kaggle')
        self.cardea = Cardea(data_path, True)
        self.label_times = self.cardea.label(prediction_problem_function)
        self.cardea.fit(self.X, self.y)

    def test__load_entityset(self):
        es = self.cardea.entityset
        assert len(es.entities) == 9
        assert len(es.relationships) == 6

    def test_list_labelers(self):
        labelers = self.cardea.list_labelers()
        assert isinstance(labelers, set)

    def test_label(self):
        assert len(self.label_times) == 100

    def test_featurize(self):
        label_times = self.label_times.iloc[:10]
        feature_matrix = self.cardea.featurize(label_times)
        assert len(feature_matrix) == 10

    def test_set_pipeline(self):
        pipeline = "Random Forest"
        self.cardea.set_pipeline(pipeline)

    def test_fit(self):
        self.cardea.fit(self.X, self.y)

    def test_predict(self):
        y = self.cardea.predict(self.X)
        assert self.y.shape == y.shape

    def test_fit_predict(self):
        y = self.cardea.fit_predict(self.X, self.y)
        assert self.y.shape == y.shape

    def test_train_test_split(self):
        X_train, X_test, y_train, y_test = self.cardea.train_test_split(self.X, self.y)
        assert X_train.shape[1] == X_test.shape[1]
        assert len(X_train) == len(y_train)
        assert len(X_test) == len(y_test)

    def test_evaluate(self):
        results = self.cardea.evaluate(self.X, self.y)
        assert isinstance(results, pd.Series)
        assert len(results) == 4

    def test_evaluate_fit(self):
        results = self.cardea.evaluate(self.X, self.y, fit=True)
        assert isinstance(results, pd.Series)
        assert len(results) == 4

    def test_save_load(self, tmpdir):
        path = os.path.join(tmpdir, 'some/path.pkl')
        self.cardea.save(path)

        new_cardea = Cardea.load(path)
        assert new_cardea.entityset == self.cardea.entityset
