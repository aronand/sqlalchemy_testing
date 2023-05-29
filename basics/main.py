from pathlib import Path

from sqlalchemy import create_engine

import models


def main() -> None:
    db_file = Path.cwd() / "test.db"
    engine = create_engine(f"sqlite:///{db_file.name}", echo=True)
    if not db_file.exists():
        models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
