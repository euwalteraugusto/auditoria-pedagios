import os
import pandas as pd
from typing import Optional, Union


def load_file(
    file_path: str,
    sheet_name: Optional[Union[str, int]] = None
) -> pd.DataFrame:
    """
    Carrega arquivos de dados (.xlsx, .csv) e retorna um DataFrame.
    Responsabilidade exclusiva: leitura do arquivo.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    _, ext = os.path.splitext(file_path.lower())

    try:
        if ext == ".xlsx":
            df = pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                engine="openpyxl"
            )

        elif ext == ".csv":
            df = pd.read_csv(
                file_path,
                sep=";",
                encoding="utf-8"
            )

        else:
            raise ValueError(
                f"Formato de arquivo não suportado ({ext}). "
                "Utilize .xlsx ou .csv"
            )

    except Exception as e:
        raise RuntimeError(
            f"Falha ao carregar arquivo: {file_path}"
        ) from e

    if df.empty:
        raise ValueError("Arquivo carregado, porém sem registros.")

    return df
