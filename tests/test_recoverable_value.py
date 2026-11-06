import pandas as pd
import pytest

from src.audit.rules.duplicate_passages import find_duplicate_passages
from src.audit.rules.recoverable_value import calculate_recoverable_value


def test_valor_recuperavel_e_quantidade_menos_um_vezes_valor(df_passagens):
    duplicados, _ = find_duplicate_passages(df_passagens)

    consolidado, total = calculate_recoverable_value(duplicados)

    assert len(consolidado) == 2
    por_placa = consolidado.set_index("PLACA")
    assert por_placa.loc["AAA1A11", "QTD_OCORRENCIAS"] == 3
    assert por_placa.loc["AAA1A11", "VALOR_RECUPERAVEL"] == pytest.approx(20.0)
    assert por_placa.loc["BBB2B22", "QTD_OCORRENCIAS"] == 2
    assert por_placa.loc["BBB2B22", "VALOR_RECUPERAVEL"] == pytest.approx(5.5)
    assert total == pytest.approx(25.5)


def test_dataframe_vazio_retorna_zero():
    consolidado, total = calculate_recoverable_value(pd.DataFrame())

    assert consolidado.empty
    assert total == 0.0


def test_recuperavel_menor_que_total_duplicado(df_passagens):
    duplicados, total_duplicado = find_duplicate_passages(df_passagens)

    _, total_recuperavel = calculate_recoverable_value(duplicados)

    assert 0 < total_recuperavel < total_duplicado
