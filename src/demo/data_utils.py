import pandas as pd

def calcular_promedio(df: pd.DataFrame, columna: str) -> float:
    """
    Calcula el promedio de una columna numérica en un DataFrame.
    """
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    return df[columna].mean()