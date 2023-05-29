from pathlib import Path

from sqlalchemy import create_engine, Engine

import models


class Program:
    def __init__(self):
        self.db_file = Path.cwd() / "test.db"
        self.engine: None | Engine = None

    def startup(self) -> None:
        self.engine = create_engine(f"sqlite:///{self.db_file.name}", echo=True)
        self.db_file.exists() or self.create_database()  # equivalent to if not exists [...]

    def create_database(self) -> None:
        models.Base.metadata.create_all(self.engine)


if __name__ == "__main__":
    p = Program()
    p.startup()
