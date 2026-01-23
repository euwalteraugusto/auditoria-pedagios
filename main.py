import pandas as pd
import os
"""
Importa funções para:
- Carregar arquivo
- Validar colunas obrigatórias
- Normalizar dados
- Encontrar passagens duplicadas
- Calcular valor recuperável
- Exportar relatório de auditoria
"""
from src.loaders.file_loader import load_file
from src.loaders.validators.schema_validator import validate_required_columns
from src.loaders.validators.processors.normalizer import normalize_dataframe
from src.audit.rules.duplicate_passages import find_duplicate_passages
from src.audit.rules.recoverable_value import calculate_recoverable_value
from src.exporters.excel_exporter import export_audit_report

# Lista de Colunas obrigatórias após normalização
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
        return (
            df
            .sort_values(by=["PLACA", "DATA PASSAGEM"])
            .reset_index(drop=True)
        )
    
    raise ValueError(
            "Colunas obrigatórias PLACA e/ou DATA PASSAGEM ausentes para auditoria."
        )


def get_audit_config():
    return {
        "file_path": r"V:\T_Embarcada\#PEDAGIO\QUIMICO\SEM PARAR_ FATURA QUIMICO 30.01.2026.xlsx",
        "sheet_name": "PASSAGENS PEDÁGIO",
        "required_columns": REQUIRED_COLUMNS
    }
    
def prepare_dataframe(file_path: str, sheet_name: str, required_columns: list) -> pd.DataFrame:
    df = load_file(file_path, sheet_name=sheet_name)
    df = normalize_dataframe(df)
    validate_required_columns(df, required_columns)
    
    return preprocess_for_audit(df) 
    
def run_duplicate_audit(df: pd.DataFrame) -> dict:
    duplicates_df, duplicated_value = find_duplicate_passages(df)
    recoverable_df, recoverable_value = calculate_recoverable_value(duplicates_df)
    
    return {
        "duplicates_df": duplicates_df,
        "recoverable_df": recoverable_df,
        "total_duplicated": duplicated_value,
        "total_recoverable": recoverable_value
    }
    
def export_results(
    base_df: pd.DataFrame,
    audit_results: dict,
    source_file_path: str
):
    base_name = os.path.splitext(os.path.basename(source_file_path))[0]
    output_file = f"RELATÓRIO AUDITORIA {base_name}.xlsx"

    export_audit_report(
        output_path=output_file,
        base_df=base_df,
        duplicates_df=audit_results["duplicates_df"],
        recoverable_df=audit_results["recoverable_df"],
        total_duplicated=audit_results["total_duplicated"],
        total_recoverable=audit_results["total_recoverable"]
    )

def main():
    config = get_audit_config()

    df = prepare_dataframe(
        file_path=config["file_path"],
        sheet_name=config["sheet_name"],
        required_columns=config["required_columns"]
    )

    audit_results = run_duplicate_audit(df)

    export_results(
        base_df=df,
        audit_results=audit_results,
        source_file_path=config["file_path"]
    )

    print("Auditoria concluída com sucesso.")

if __name__ == "__main__":
    main()
