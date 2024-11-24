from typing import Callable
from typing import Generic
from typing import TypeVar

from pathlib import Path
from sqlite3 import Connection


A = TypeVar("A")
R = TypeVar("R")


class Sql(Generic[A, R]):
    query: Path

    def __init__(self, connection: Connection) -> None: ...

    def __call__(self, args: A) -> R: ...
