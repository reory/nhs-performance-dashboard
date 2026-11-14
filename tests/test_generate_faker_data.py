from datetime import UTC, date, datetime
from unittest.mock import MagicMock

import scripts.generate_faker_data as gen


def test_generate_pilot_data(monkeypatch):
    """Verify generated patient data is written to DuckDB."""

    # Mock DuckDB connection
    fake_con = MagicMock()
    fake_con.execute.return_value = None
    fake_con.executemany.return_value = None
    monkeypatch.setattr(gen, "con", fake_con)

    # Mock NHS number generator
    monkeypatch.setattr(
        gen.nhs_number, 
        "generate", 
        lambda quantity=1, for_region=None, **kwargs: ["1234567890"] * quantity,
    )

    fake_faker = MagicMock()
    fake_faker.date_between.return_value = date(2025, 1, 23)
    fake_faker.date_of_birth.return_value = date(1976, 1, 3)
    fake_faker.name.return_value = "Harry Broth"

    monkeypatch.setattr(gen, "fake", fake_faker)

    # Mock random choice to return deterministic values
    monkeypatch.setattr(gen.random, "choice", lambda seq: seq[0])

    # Mock TQDM so it does not loop visually
    monkeypatch.setattr(gen, "tqdm", lambda x, **kwargs: x)

    # Mock datetime.now()
    class FakeDateTime:
        """Mock datetime returning a fixed timestamp."""

        @staticmethod
        def now(tz=UTC, **kwargs):
            return datetime(2025, 1, 30, tzinfo=UTC)  # 1 week after ref_date

    monkeypatch.setattr(gen, "datetime", FakeDateTime)

    # Run the generator with a small number
    gen.generate_pilot_data(n=3)

    # Table creation called
    assert fake_con.execute.called

    # Bulk insert called once
    assert fake_con.executemany.called

    # Check inserted rows
    args, _ = fake_con.executemany.call_args
    inserted_rows = args[1]
    assert len(inserted_rows) == 3

    # Check one row structure
    row = inserted_rows[0]
    assert row[0] in gen.gp_practices
    assert row[1] == "1234567890"
    assert row[2] == "Harry Broth"
    assert isinstance(row[3], date)
    assert row[4] in gen.specialties
    assert row[5] in gen.priorities
    assert isinstance(row[6], date)
    assert isinstance(row[7], int)
