import pandas as pd
from typing import List


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: List[str]
) -> None:
    """
    Valida se o DataFrame contém todas as colunas obrigatórias
    e se elas possuem ao menos um valor não nulo.
    
    (Falha por exceção)
    """

    df_columns = set(df.columns)
    required = set(required_columns)

    missing_columns = required - df_columns

    if missing_columns:
        raise ValueError(
            "Validação de schema falhou.\n"
            f"Colunas obrigatórias ausentes: {sorted(missing_columns)}\n"
            f"Colunas encontradas: {sorted(df_columns)}"
        )

    # Verifica colunas vazias (100% nulas)
    empty_columns = [
        col for col in required
        if df[col].isna().all()
    ]

    if empty_columns:
        raise ValueError(
            "Validação de schema falhou.\n"
            f"Colunas obrigatórias sem dados: {sorted(empty_columns)}"
        )
