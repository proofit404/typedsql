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


# @todo #1 Setup PostgreSQL in docker-compose project.

# @todo #1 Setup PostgreSQL in github actions.

# @todo #1 Setup MySQL in docker-compose project.

# @todo #1 Setup MySQL in github actions.

# @todo #1 Fetch database roles.
#  Add callable interface which could produce selected rows of
#  concrete type.

# @todo #1 Asynchronous fetch database roles.
#  Depending on result type is a collection or not we should use fetch
#  or fetch all engine method under the hood.
