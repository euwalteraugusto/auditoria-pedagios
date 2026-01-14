import pandas as pd


def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza tipos e formatos do DataFrame:
    - Strings: strip + upper -> remove espaços em branco e converte str maiúsculas
    - Datas: DATA PASSAGEM em datatime
    - Valores monetários: float padrão
    - Valida presença de NaT em DATA PASSAGEM
    
    :param df: DataFrame carregado
    :return: DataFrame normalizado
    """
    
    df = df.copy() # Evita efeito colateral
    
    # 1. Normalizar strings (todas as colunas object(texto))
    string_cols = df.select_dtypes(include="object").columns
    for col in string_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.upper()
        )
        
    # 2. Validar e padronizar DATA PASSAGEM
    if "DATA PASSAGEM" in df.columns:
        # Coerce (conversão de tipos) já foi feito no loader, mas garante tipo datatime
        df["DATA PASSAGEM"] = pd.to_datetime(df["DATA PASSAGEM"], errors="coerce", dayfirst=True)
        
        # Verifica NaT
        if df["DATA PASSAGEM"].isna().any():
            raise ValueError("Existem datas inválidas em DATA PASSAGEM. Corrija o arquivo de entrada.")
    else:
        raise ValueError("Coluna DATA PASSAGEM n]ao encontrada após carregamento.")
    
    # 3. Normalizar valores monetários
    if "VALOR" in df.columns:
        df["VALOR"] = (
            df["VALOR"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace("[^0-9.]", "", regex=True)
            .astype(float)
        ) 
        
    return df