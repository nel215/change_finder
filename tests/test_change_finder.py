# coding: utf-8
from change_finder import ChangeFinder, SDAR
import numpy as np


def test_sdar_update():
    sdar = SDAR()
    sdar.update(1.0)
    assert sdar.x[0] == 1.0
    sdar.update(2.0)
    assert sdar.x[0] == 2.0
    assert sdar.x[1] == 1.0


def test_cf_update():
    np.random.seed(0)
    points = np.concatenate([
        np.random.normal(1, 0.1, 100),
        np.random.normal(-1, 0.1, 100),
    ])
    cf = ChangeFinder()
    for i, p in enumerate(points):
        cf.update(p)
