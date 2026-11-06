import pandas as pd
import pytest

from src.loaders.validators.processors.normalizer import normalize_dataframe


def test_cria_data_passagem_a_partir_de_data_e_hora():
    df = pd.DataFrame(
        {"DATA": ["15/03/2024"], "HORA": ["08:30"], "PLACA": ["abc1d23"], "VALOR": ["10"]}
    )

    resultado = normalize_dataframe(df)

    assert resultado.loc[0, "DATA PASSAGEM"] == pd.Timestamp("2024-03-15 08:30")


def test_normaliza_texto_para_maiusculas_sem_espacos():
    df = pd.DataFrame(
        {
            "DATA PASSAGEM": ["2024-03-15"],
            "PLACA": ["  abc1d23 "],
            "PRAÇA": [" praça central"],
            "VALOR": [1],
        }
    )

    resultado = normalize_dataframe(df)

    assert resultado.loc[0, "PLACA"] == "ABC1D23"
    assert resultado.loc[0, "PRAÇA"] == "PRAÇA CENTRAL"


def test_converte_valor_com_virgula_e_simbolo_monetario():
    df = pd.DataFrame({"DATA PASSAGEM": ["2024-03-15", "2024-03-16"], "VALOR": ["R$ 12,50", "3,00"]})

    resultado = normalize_dataframe(df)

    assert resultado["VALOR"].tolist() == [12.5, 3.0]


def test_nao_altera_dataframe_original():
    df = pd.DataFrame({"DATA PASSAGEM": ["2024-03-15"], "PLACA": [" abc "], "VALOR": ["1,5"]})
    copia = df.copy()

    normalize_dataframe(df)

    pd.testing.assert_frame_equal(df, copia)


def test_sem_data_passagem_nem_data_hora_levanta_erro():
    with pytest.raises(ValueError, match="DATA PASSAGEM"):
        normalize_dataframe(pd.DataFrame({"VALOR": ["1"]}))


def test_data_invalida_levanta_erro():
    df = pd.DataFrame({"DATA PASSAGEM": ["não-é-data"], "VALOR": ["1"]})

    with pytest.raises(ValueError, match="DATA PASSAGEM inválida"):
        normalize_dataframe(df)


def test_valor_invalido_levanta_erro():
    df = pd.DataFrame({"DATA PASSAGEM": ["2024-03-15"], "VALOR": ["abc"]})

    with pytest.raises(ValueError, match="VALOR"):
        normalize_dataframe(df)
