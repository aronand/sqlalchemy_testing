from pathlib import Path
from typing import Callable

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session

import models


class Program:
    def __init__(self):
        self.db_file = Path.cwd() / "test.db"
        self.engine: None | Engine = None
        self.running = False

    def startup(self) -> None:
        self.engine = create_engine(f"sqlite:///{self.db_file.name}", echo=True)
        self.db_file.exists() or self.create_database()  # equivalent to if not exists [...]

    def create_database(self) -> None:
        models.Base.metadata.create_all(self.engine)

    def run(self) -> None:
        commands: dict[str, Callable] = {
            "create": self.create_user,
            "edit": lambda: print("Not implemented"),
            "delete": lambda: print("Not implemented"),
            "list": lambda: print("Not implemented"),
            "show": lambda: print("Not implemented"),
            "export": lambda: print("Not implemented"),
            "exit": self.stop
        }

        self.running = True
        print(f"Available commands are: {', '.join([key for key in commands.keys()])}")
        while self.running:
            command = input("cmd: ").lower()
            if command == "exit":
                break
            if command not in commands:
                print("Invalid command")
                continue
            commands[command]()

    def stop(self) -> None:
        self.running = False

    def create_user(self) -> None:
        name = input("Name: ")
        fullname = input("Full name: ")

        with Session(self.engine) as session:
            new_user = models.User(
                name=name,
                fullname=fullname,
            )

            session.add(new_user)
            session.commit()


if __name__ == "__main__":
    p = Program()
    p.startup()
    p.run()
