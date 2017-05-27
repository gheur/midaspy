import pytest
import numpy as np

from midas.weights import beta_weights_es, x_weighted


def test_beta_es():
    w = beta_weights_es(3, 1, 5)

    assert np.allclose(w,[0.941176, 0.0588238, 9.4118e-25])


def test_x_weighted():
    x = np.ones((3, 3))

    xw, w = x_weighted(x, 1., 5.)

    assert x.shape[0] == xw.shape[0]
    assert np.allclose(xw, [1., 1., 1.])
