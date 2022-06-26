import pytest
import src.mlp


def test_mlp1():
    x = [1, 0.5, 1.3, 0.6]
    w = [[0.2, 0.4],
         [-1.2, 2.3],
         [0.5, -0.5],
         [1.1, 2]]
    assert src.mlp.salida_capa(
        x, w) == [0.7130001627522816, 0.8909031788043871]
