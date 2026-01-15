import pandas as pd


TEXT_COLUMNS = [
    "PLACA",
    "PRAÇA"
]


def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza e padroniza o DataFrame para auditoria.
    """

    df = df.copy()

    # 1. Criar DATA PASSAGEM
    if "DATA PASSAGEM" not in df.columns:
        if {"DATA", "HORA"}.issubset(df.columns):
            df["DATA PASSAGEM"] = pd.to_datetime(
                df["DATA"].astype(str).str.strip()
                + " "
                + df["HORA"].astype(str).str.strip(),
                errors="coerce",
                dayfirst=True
            )
        else:
            raise ValueError(
                "Não foi possível criar DATA PASSAGEM: "
                "colunas DATA e HORA ausentes."
            )

    df["DATA PASSAGEM"] = pd.to_datetime(
        df["DATA PASSAGEM"],
        errors="coerce",
        dayfirst=True
    )

    if df["DATA PASSAGEM"].isna().any():
        raise ValueError(
            "Existem registros com DATA PASSAGEM inválida."
        )

    # 2. Normalizar colunas textuais conhecidas
    for col in TEXT_COLUMNS:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.upper()
            )

    # 3. Normalizar VALOR
    if "VALOR" in df.columns:
        df["VALOR"] = (
            df["VALOR"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace(r"[^0-9.]", "", regex=True)
        )

        df["VALOR"] = pd.to_numeric(
            df["VALOR"],
            errors="coerce"
        )

        if df["VALOR"].isna().any():
            raise ValueError(
                "Existem valores inválidos na coluna VALOR."
            )

    return df
