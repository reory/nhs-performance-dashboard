import importlib
from unittest.mock import MagicMock
import builtins
import scripts.view_all as view_module


def test_view_all_script(monkeypatch):

    # Fake DuckDB connection
    fake_con = MagicMock()
    fake_con.execute.return_value = None

    # Patch duckdb.connect BEFORE reloading the module
    monkeypatch.setattr(view_module.duckdb, "connect", lambda _: fake_con)

    # Patch built-in print so it doesn't output
    monkeypatch.setattr(builtins, "print", lambda *args, **kwargs: None)

    # Reload module so the top-level code runs with mocks
    importlib.reload(view_module)

    # Assertions
    fake_con.execute.assert_called_once()
