import pandas as pd

def export_audit_report(
    output_path: str,
    base_df: pd.DataFrame,
    duplicates_df: pd.DataFrame,
    recoverable_df: pd.DataFrame,
    total_duplicated: float,
    total_recoverable: float
) -> None:
    """
    Exporta o relatório completo de auditoria para Excel.
    """

    resumo = pd.DataFrame({
        "Indicador": [
            "Total de registros analisados",
            "Total de registros duplicados",
            "Valor total duplicado",
            "Valor efetivamente recuperável"
        ],
        "Valor": [
            len(base_df),
            len(duplicates_df),
            total_duplicated,
            total_recoverable
        ]
    })

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        base_df.to_excel(
            writer,
            sheet_name="BASE_NORMALIZADA",
            index=False
        )

        duplicates_df.to_excel(
            writer,
            sheet_name="DUPLICADOS_DETALHE",
            index=False
        )

        recoverable_df.to_excel(
            writer,
            sheet_name="RECUPERAVEL_RESUMO",
            index=False
        )

        resumo.to_excel(
            writer,
            sheet_name="RESUMO_EXECUTIVO",
            index=False
        )
