# -*- coding: utf-8 -*-

import numpy as np
from scipy.fftpack import fft

# Audio featurization functions.
EPSILON = 0.00000001


def energy(data):
    """Computes signal energy of data"""
    data = np.mean(data, axis=1)
    return np.sum(data ** 2) / np.float64(len(data))


def FFT(data, nFFT):
    X = abs(fft(data))                                  # get fft magnitude
    X = X[0:nFFT]                                    # normalize fft
    return X // len(X)


def spectral_entropy(data, numOfShortBlocks=10):
    """Computes the spectral entropy"""
    data = np.mean(data, axis=1)

    nFFT = len(data) // 2
    X = FFT(data, nFFT)
    L = len(X)                         # number of frame data
    Eol = np.sum(X ** 2)            # total spectral energy

    subWinLength = int(np.floor(L / numOfShortBlocks))   # length of sub-frame
    if L != subWinLength * numOfShortBlocks:
        X = X[0:subWinLength * numOfShortBlocks]

    # define sub-frames (using matrix reshape)
    subWindows = X.reshape(subWinLength, numOfShortBlocks, order='F').copy()

    # compute spectral sub-energies
    s = np.sum(subWindows ** 2, axis=0) / (Eol + EPSILON)

    # compute spectral entropy
    return -np.sum(s * np.log2(s + EPSILON))


def rand_attr1(data):
    data = np.array(data)
    flattened = np.mean(data, axis=1)
    return np.std(flattened)


def zcr(data):
    """Computes zero crossing rate of segment"""
    data = np.mean(data, axis=1)

    count = len(data)
    countZ = np.sum(np.abs(np.diff(np.sign(data)))) / 2
    return (np.float64(countZ) / np.float64(count - 1.0))


def spectral_flux(d0, d1):
    """
    Computes the spectral flux feature of the current frame
    """
    # compute the spectral flux as the sum of square distances:
    d0 = np.mean(d0, axis=1)
    d1 = np.mean(d1, axis=1)
    nFFT = min(len(d0) // 2, len(d1) // 2)
    X = FFT(d0, nFFT)
    Xprev = FFT(d1, nFFT)

    # L = min(len(X), len(Xprev))

    sumX = np.sum(X + EPSILON)
    sumPrevX = np.sum(Xprev + EPSILON)
    return np.sum((X / sumX - Xprev / sumPrevX) ** 2)


def energy_entropy(data, fs, numOfShortBlocks=10):
    """Computes entropy of energy"""
    data = np.mean(data, axis=1)

    Eol = np.sum(data ** 2)    # total data energy
    L = len(data)
    subWinLength = int(np.floor(L / numOfShortBlocks))
    if L != subWinLength * numOfShortBlocks:
        data = data[0:subWinLength * numOfShortBlocks]

    # subWindows is of size [numOfShortBlocks x L]
    subWindows = data.reshape(subWinLength, numOfShortBlocks, order='F').copy()

    # Compute normalized sub-data energies:
    s = np.sum(subWindows ** 2, axis=0) / (Eol + EPSILON)

    # Compute entropy of the normalized sub-data energies:
    Entropy = -np.sum(s * np.log2(s + EPSILON))
    return Entropy


def spectral_centroid_and_spread(data, fs):
    """Computes spectral centroid of frame (given abs(FFT))"""
    data = np.mean(data, axis=1)

    nFFT = len(data) // 2
    X = FFT(data, nFFT)

    ind = (np.arange(1, len(X) + 1)) * (fs / (2.0 * len(X)))

    Xt = X.copy()
    Xt = Xt / Xt.max()
    NUM = np.sum(ind * Xt)
    DEN = np.sum(Xt) + EPSILON

    # Centroid:
    C = (NUM / DEN)

    # Spread:
    S = np.sqrt(np.sum(((ind - C) ** 2) * Xt) / DEN)

    # Normalize:
    C = C / (fs / 2.0)
    S = S / (fs / 2.0)

    return (C, S)


def spectral_rolloff(data, coeff):
    """Computes spectral roll-off"""
    data = np.mean(data, axis=1)
    nFFT = len(data) // 2
    X = FFT(data, nFFT)

    totalEnergy = np.sum(X ** 2)
    fftLength = len(X)
    Thres = coeff * totalEnergy

    # Find the spectral rolloff as the frequency position where the
    # respective spectral energy is equal to c*totalEnergy
    CumSum = np.cumsum(X ** 2) + EPSILON
    [a, ] = np.nonzero(CumSum > Thres)
    if len(a) > 0:
        mC = np.float64(a[0]) / (float(fftLength))
    else:
        mC = 0.0

    return mC


def featurize_segments(segments, sample_frequency):
    features = []
    for i in range(len(segments) - 1):
        segment = segments[i]
        centroid_and_spread = spectral_centroid_and_spread(segment, sample_frequency)
        features.extend([
            energy(segment),
            energy_entropy(segment, sample_frequency),
            spectral_entropy(segment),
            spectral_flux(segment, segments[i + 1]),
            centroid_and_spread[0],
            centroid_and_spread[1],
            spectral_rolloff(segment, .90),
            rand_attr1(segment),
            zcr(segment)
        ])

    return features


def featurize_audio(X, sample_frequencies):
    audio_features = []

    # Featurize
    for segments, sample_frequency in zip(X, sample_frequencies):
        features = featurize_segments(segments, sample_frequency)
        audio_features.append(features)

    return audio_features
