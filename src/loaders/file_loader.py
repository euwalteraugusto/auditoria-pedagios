import os
import pandas as pd
from typing import Optional, Union


def load_file(file_path: str, sheet_name: Optional[Union[str, int]] = None) -> pd.DataFrame:
    """
    Carrega arquivos de dados (.xlsx, .csv) e retorna um DataFrame.
    
    Responsabilidades:
    - Verificar se o arquivo existe
    - Ler o arquivo Excel
    - Retornar os dados em formato estruturado
    
    :param file_path: Caminho completo do arquivo Excel
    :param sheet_name: Nome da aba (opcional)
    :return: pandas.DataFrame com os dados carregados
    """
    
    # 1. Verificar se o arquivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    _, ext = os.path.splitext(file_path.lower()) # "_," ignora o nome do arquivo -> "ext" guarda apenas a extensão
    
    # 2. Ler o arquivo [.xlsx, .csv]
    try:
        if ext == ".xlsx":
            df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl") # Se a extensão for .xlsx -> lê o arquivo excel através do openpyxl
            
        elif ext == ".csv":
            df = pd.read_csv(file_path, sep=";", encoding="utf-8") # Se a ext for .csv -> lê o arquivo através do encondind="utf-8"
            
        else:
            raise ValueError(f"Formato de arquivo não suportado ({ext}). ""Converta o arquivo para .xlsx ou .csv")
        
    except Exception as e:
        raise ValueError(f"Erro ao ler arquivo ({ext}): {e}")
    
    # 3. Validar se o arquivo não está vazio
    if df.empty:
        raise ValueError("O arquivo está vazio.")
    
    # 4. Unificar DATA + HORA em DATA PASSAGEM
    if {"DATA", "HORA"}.issubset(df.columns):
        df["DATA PASSAGEM"] = pd.to_datetime(
            df["DATA"].astype(str).str.strip() + " " +
            df["HORA"].astype(str).str.strip(),
            errors="coerce",
            dayfirst=True
        )
    else:
        raise ValueError(
            "Layout inválido: coluna obrigatórias DATA e/ou HORA não encontradas."
        )
    
    return df