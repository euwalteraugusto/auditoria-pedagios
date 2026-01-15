import pandas as pd
from typing import List, Tuple

DUPLICATE_KEYS: List[str] = [
    "PLACA",
    "PRAÇA",
    "DATA PASSAGEM",
    "VALOR"
]

def calculate_recoverable_value(
    duplicates: pd.DataFrame
) -> Tuple[pd.DataFrame, float]:
    """
    Calcula o valor efetivamente recuperável a partir
    das passagens duplicadas.

    Retorna:
    - DataFrame consolidado por chave de duplicidade
    - Valor total recuperável
    """

    if duplicates.empty:
        return pd.DataFrame(), 0.0

    grouped = (
        duplicates
        .groupby(DUPLICATE_KEYS)
        .size()
        .reset_index(name="QTD_OCORRENCIAS")
    )

    # Recuperável = (quantidade - 1) * valor
    grouped["VALOR_RECUPERAVEL"] = (
        (grouped["QTD_OCORRENCIAS"] - 1) * grouped["VALOR"]
    )

    total_recoverable = grouped["VALOR_RECUPERAVEL"].sum()

    return grouped, total_recoverable
