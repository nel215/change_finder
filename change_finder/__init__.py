# coding: utf-8
from scipy.linalg import solve_toeplitz
from scipy.stats import norm
import numpy as np


class SDAR(object):
    def __init__(self, r=0.9, k=5):
        self.r = r
        self.k = k
        self.C = np.zeros(k+1)
        self.x = np.zeros(k+1)
        self.mu = 0.0
        self.sigma = 0.0

    def update(self, x):
        self.x = np.roll(self.x, 1)
        self.x[0] = x
        self.mu = (1.0 - self.r) * self.mu + self.r * x
        self.C = (1.0 - self.r) * self.C
        self.C += self.r * (x - self.mu) * (self.x - self.mu)
        A = solve_toeplitz(self.C[:-1], self.C[1:])
        pred = np.dot(A, self.x[1:] - self.mu) + self.mu
        self.sigma = (1.0 - self.r) * self.sigma + self.r * (x - pred)**2
        return -np.log(norm.pdf(x=x, loc=pred, scale=self.sigma**0.5))


class ChangeFinder(object):
    def __init__(self, r=0.005, k=2, T=5, R=2):
        self.first_sdar = SDAR(r, k)
        self.second_sdar = SDAR(r, k)
        self.first_scores = np.zeros(T)
        self.second_scores = np.zeros(R)

    def update(self, x):
        x = float(x)
        self.first_scores = np.roll(self.first_scores, 1)
        self.first_scores[0] = self.first_sdar.update(x)
        self.second_scores = np.roll(self.second_scores, 1)
        self.second_scores[0] = self.second_sdar.update(
            np.mean(self.first_scores))
        return np.mean(self.second_scores)
