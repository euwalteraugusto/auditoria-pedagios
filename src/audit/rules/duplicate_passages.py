import pandas as pd
from typing import List, Tuple


DUPLICATE_KEYS: List[str] = [
    "PLACA",
    "PRAÇA",
    "DATA PASSAGEM",
    "VALOR"
]


def find_duplicate_passages(
    df: pd.DataFrame
) -> Tuple[pd.DataFrame, float]:
    """
    Identifica passagens de pedágio duplicadas.

    Regra:
    - Mesma PLACA
    - Mesma PRAÇA
    - Mesma DATA PASSAGEM
    - Mesmo VALOR

    Retorna:
    - DataFrame com registros duplicados
    - Valor total duplicado
    """

    missing = set(DUPLICATE_KEYS) - set(df.columns)
    if missing:
        raise ValueError(
            "Colunas necessárias para auditoria de duplicidade ausentes: "
            f"{sorted(missing)}"
        )

    duplicates = df[df.duplicated(
        subset=DUPLICATE_KEYS,
        keep=False
    )]

    if duplicates.empty:
        return pd.DataFrame(columns=df.columns), 0.0

    duplicates = (
        duplicates
        .sort_values(by=DUPLICATE_KEYS)
        .reset_index(drop=True)
    )

    total_duplicated_value = duplicates["VALOR"].sum()

    return duplicates, total_duplicated_value
