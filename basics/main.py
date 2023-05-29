from pathlib import Path

from sqlalchemy import create_engine, Engine

import models


def main() -> None:
    db_file = Path.cwd() / "test.db"
    engine = create_engine(f"sqlite:///{db_file.name}", echo=True)
    db_file.exists() or create_database(engine)  # equivalent to if not exists [...]


def create_database(engine: Engine) -> None:
    models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
