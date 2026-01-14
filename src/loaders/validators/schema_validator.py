import pandas as pd
from typing import List


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: List[str]
) -> None:
    """
    (Função de Validação -> Sem retorno)
    Valida se o DataFrame contém todas as colunas obrigatórias.
    
    :param df: DataFrame carregado
    :param required_columns: Lista de colunas obrigatórias
    :raises ValueError: se alguma coluna estiver ausente -> Falha por excessão
    """
    
    # Colunas existentes no DataFrame
    df_columns = set(df.columns)
    
    # Colunas obrigatórias
    required = set(required_columns)
    
    # Diferença: o que é obrigatório e não existe no DF
    missing_columns = required - df_columns
    
    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {sorted(missing_columns)}"
        )