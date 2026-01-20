import pandas as pd

from src.loaders.file_loader import load_file
from src.loaders.validators.schema_validator import validate_required_columns
from src.loaders.validators.processors.normalizer import normalize_dataframe
from src.audit.rules.duplicate_passages import find_duplicate_passages
from src.audit.rules.recoverable_value import calculate_recoverable_value
from src.exporters.excel_exporter import export_audit_report

# Colunas obrigatórias após normalização
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


def main():
    caminho_arquivo = (
        r"V:\T_Embarcada\#PEDAGIO\QUIMICO\SEM PARAR_ FATURA QUIMICO 20.01.2026.xlsx"
    )
    aba = "PASSAGENS PEDÁGIO"
    
    # 1. Carregar arquivo
    df = load_file(caminho_arquivo, sheet_name=aba)
    
    # 2. Normalizar dados (cria DATA PASSAGEM a partir de DATA + HORA)
    df = normalize_dataframe(df)
    
    # 3. Validar colunas obrigatórias
    validate_required_columns(df, REQUIRED_COLUMNS)
    
    # 4. Pré-processamento para auditoria
    df = preprocess_for_audit(df)
    
    # 5. Conferência
    print("Dados prontos para auditoria.")
    print(df.dtypes)
    print(df.head())
    
    # 6. Auditoria de duplicidade
    df_duplicates, duplicated_value = find_duplicate_passages(df)
    
    print("\nAuditoria de duplicidade:")
    print(f"Registros duplicados: {len(df_duplicates)}")
    print(f"Valor total duplicado: R$ {duplicated_value:,.2f}")

    if df_duplicates.empty:
        print("Nenhuma passagem duplicada encontrada.")
    else:
        print("Passagens duplicadas encontradas:")
        print(df_duplicates)
        
    # 7. Cálculo do valor recuperável
    recoverable_df, recoverable_value = calculate_recoverable_value(df_duplicates)

    print(f"Valor efetivamente recuperável: R$ {recoverable_value:,.2f}")

    # 8. Exportação
    output_file = "RELATÓRIO AUDITORIA SEM PARAR_ FATURA QUIMICO 20.01.2026.xlsx"

    export_audit_report(
        output_path=output_file,
        base_df=df,
        duplicates_df=df_duplicates,
        recoverable_df=recoverable_df,
        total_duplicated=duplicated_value,
        total_recoverable=recoverable_value
    )

    print(f"Relatório exportado com sucesso: {output_file}")


if __name__ == "__main__":
    main()
