"""Test data utility functions."""

import pandas as pd
import pytest
from src.demo.data_utils import calcular_promedio

def test_promedio_correcto():
    df = pd.DataFrame({"nota": [80, 90, 100]})
    assert calcular_promedio(df, "nota") == 90

def test_columna_inexistente():
    df = pd.DataFrame({"nota": [80, 90, 100]})
    with pytest.raises(ValueError):
        calcular_promedio(df, "edad")

def test_promedio_incorrecto():
    df = pd.DataFrame({"nota": [80, 90, 100]})
    assert calcular_promedio(df, "nota") == 95