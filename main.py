from src.loaders.file_loader import load_file

def main():
    caminho_arquivo = r"V:\T_Embarcada\#PEDAGIO\QUIMICO\LANÇADAS\FATURAS EXCEL\SEM PARAR_ FATURA QUIMICO 30.10.2025.xlsx"
    # "r" diz ao Python: "não interprete barras invertidas"
    aba = "PASSAGENS PEDÁGIO"
    df = load_file(caminho_arquivo, sheet_name=aba)
    print(df.head())
    
if __name__ == "__main__":
    main()
    
from src.loaders.file_loader import load_file
from src.loaders.validators.schema_validator import validate_required_columns


REQUIRED_COLUMNS = [
    "PLACA",
    "DATA",
    "HORA",
    "PRAÇA",
    "VALOR"
] 


def main():
    caminho_arquivo = r"V:\T_Embarcada\#PEDAGIO\QUIMICO\LANÇADAS\FATURAS EXCEL\SEM PARAR_ FATURA QUIMICO 30.10.2025.xlsx"
    aba = "PASSAGENS PEDÁGIO"
    
    df = load_file(caminho_arquivo, sheet_name=aba)
    validate_required_columns(df, REQUIRED_COLUMNS)
    
    print("Arquivo validado com sucesso.")
    print(df.head())
    
    
if __name__ == "__main__":
    main()
    
from src.loaders.file_loader import load_file
from src.loaders.validators.schema_validator import validate_required_columns
from src.loaders.validators.processors.normalizer import normalize_dataframe

REQUIRED_COLUMNS = [
    "PLACA",
    "DATA PASSAGEM",
    "PRAÇA",
    "VALOR"
]

def main():
    caminho_arquivo = r"V:\T_Embarcada\#PEDAGIO\QUIMICO\LANÇADAS\FATURAS EXCEL\SEM PARAR_ FATURA QUIMICO 30.10.2025.xlsx"
    aba = "PASSAGENS PEDÁGIO"
    
    df = load_file(caminho_arquivo, sheet_name=aba)
    validate_required_columns(df, REQUIRED_COLUMNS)
    # Nomralizar dados
    df = normalize_dataframe(df)
    
    # Pré-processamento para auditoria (ordenar por PLACA + DATA PASSAGEM)
    def preprocess_for_audit(df: pd.DataFrame) -> pd.DataFrame:
        """
        Pré-processa DataFrame para auditoria:
        - Ordena por PLACA + DATA PASSAGEM
        - Reseta índice
        """
        if {"PLACA", "DATA PASSAGEM"}.issubset(df.columns):
            df = df.sort_values(by=["PLACA", "DATA PASSAGEM"]).reset_index(drop=True)
        else:
            raise ValueError("Colunas obrigatórias PLACA e/ou DATA PASSAGEM ausentes para auditoria.")

        return df
    
    print("Dados normalizados com sucesso.")
    print(df.dtypes)
    print(df.head())
    
if __name__ == "__main__":
    main()
    

from src.loaders.file_loader import load_file
from src.loaders.validators.schema_validator import validate_required_columns
from src.loaders.validators.processors.normalizer import normalize_dataframe
import pandas as pd

# Definição das colunas obrigatórias
REQUIRED_COLUMNS = [
    "PLACA",
    "DATA PASSAGEM",
    "PRAÇA",
    "VALOR"
]

def preprocess_for_audit(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pré-processa DataFrame para auditoria:
    - Ordena por PLACA + DATA PASSAGEM
    - Reseta índice
    """
    if {"PLACA", "DATA PASSAGEM"}.issubset(df.columns):
        df = df.sort_values(by=["PLACA", "DATA PASSAGEM"]).reset_index(drop=True)
    else:
        raise ValueError("Colunas obrigatórias PLACA e/ou DATA PASSAGEM ausentes para auditoria.")
    return df

def main():
    # Caminho do arquivo
    caminho_arquivo = r"V:\T_Embarcada\#PEDAGIO\QUIMICO\LANÇADAS\FATURAS EXCEL\SEM PARAR_ FATURA QUIMICO 30.10.2025.xlsx"
    aba = "PASSAGENS PEDÁGIO"

    # 1️. Carregar arquivo
    df = load_file(caminho_arquivo, sheet_name=aba)

    # 2️. Validar colunas obrigatórias
    validate_required_columns(df, REQUIRED_COLUMNS)

    # 3️. Normalizar dados (strings, datas, valores)
    df = normalize_dataframe(df)

    # 4️. Pré-processamento para auditoria (ordenar + reset índice)
    df = preprocess_for_audit(df)

    # 5️. Conferir resultado
    print("Dados prontos para auditoria.")
    print(df.dtypes)
    print(df.head())

if __name__ == "__main__":
    main()
