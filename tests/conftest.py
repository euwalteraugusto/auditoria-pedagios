import sys
from pathlib import Path

import pandas as pd
import pytest

# Permite `from src...` ao rodar pytest a partir de qualquer diretório.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def df_passagens() -> pd.DataFrame:
    """Três registros idênticos (A), um par duplicado (B) e um único (C)."""
    return pd.DataFrame(
        {
            "PLACA": ["AAA1A11", "AAA1A11", "AAA1A11", "BBB2B22", "BBB2B22", "CCC3C33"],
            "PRAÇA": ["P1", "P1", "P1", "P2", "P2", "P1"],
            "DATA PASSAGEM": pd.to_datetime(
                ["2024-01-01 10:00"] * 3 + ["2024-01-02 11:00"] * 2 + ["2024-01-03 12:00"]
            ),
            "VALOR": [10.0, 10.0, 10.0, 5.5, 5.5, 7.0],
        }
    )
