import pandas as pd
import pytest

from src.audit.rules.duplicate_passages import find_duplicate_passages


def test_identifica_registros_duplicados(df_passagens):
    duplicados, total = find_duplicate_passages(df_passagens)

    assert len(duplicados) == 5  # 3 (placa A) + 2 (placa B); o registro C fica de fora
    assert set(duplicados["PLACA"]) == {"AAA1A11", "BBB2B22"}
    assert total == pytest.approx(3 * 10.0 + 2 * 5.5)


def test_resultado_ordenado_e_com_indice_reiniciado(df_passagens):
    duplicados, _ = find_duplicate_passages(df_passagens.iloc[::-1])

    assert list(duplicados.index) == list(range(len(duplicados)))
    assert duplicados["PLACA"].is_monotonic_increasing


def test_sem_duplicidade_retorna_vazio_e_zero():
    df = pd.DataFrame(
        {
            "PLACA": ["AAA1A11", "BBB2B22"],
            "PRAÇA": ["P1", "P1"],
            "DATA PASSAGEM": pd.to_datetime(["2024-01-01", "2024-01-01"]),
            "VALOR": [10.0, 10.0],
        }
    )

    duplicados, total = find_duplicate_passages(df)

    assert duplicados.empty
    assert list(duplicados.columns) == list(df.columns)
    assert total == 0.0


def test_valor_diferente_nao_e_duplicidade(df_passagens):
    df = df_passagens.copy()
    df.loc[1, "VALOR"] = 11.0  # quebra o trio da placa A -> sobram 2 iguais

    duplicados, _ = find_duplicate_passages(df)

    assert len(duplicados) == 4  # (A: 2 restantes) + (B: 2)


def test_colunas_ausentes_levanta_value_error():
    with pytest.raises(ValueError, match="ausentes"):
        find_duplicate_passages(pd.DataFrame({"PLACA": ["AAA1A11"]}))


def test_nao_modifica_dataframe_original(df_passagens):
    copia = df_passagens.copy()

    find_duplicate_passages(df_passagens)

    pd.testing.assert_frame_equal(df_passagens, copia)
