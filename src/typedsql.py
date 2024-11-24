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

# ~ @todo #1 Fetch database rows.
# ~ 
# ~ Add callable interface which could produce selected rows of
# ~ concrete type.

# ~ @todo #1 Asynchronous fetch database rows.
# ~ 
# ~ Depending on result type is a collection or not we should use fetch
# ~ or fetch all engine method under the hood.

# ~ @todo #7 Engine objects.
# ~ 
# ~ To my understanding we have to introduce `Engine`, `Connection`, or
# ~ `Driver` objects. The main reiquirement for this architecture
# ~ decision that we have to unify different `execute`, `fetch`,
# ~ `fetch_many`, and `cursor` APIs to use them inside `Sql` object.
# ~ 
# ~ We have different options here.
# ~ 
# ~ We can use `encode/databases` which already did this work for
# ~ us. My main concern is that I have a plan to support Django query
# ~ builder as well, but this project was built on top of SQLAlchemy
# ~ and has it as install requirement. Running queries built with
# ~ Django inside active SQLAlchemy connection pull using two packages
# ~ to abstract it out is a clusterfuck decission.
# ~ 
# ~ Another concern is that it would tight us to the asynchronous
# ~ world. And this is as bad as building this library on top of
# ~ SQLAlchemy engine system throwing away both SQLAlchemy ORM and
# ~ SQLAlchemy Core.
# ~ 
# ~ On the other side I don't want to abstract `asyncpg` and `mysql`
# ~ libraries into a single object. It would highly increase possibilty
# ~ of problems in the future and force us to expand it's public
# ~ interface each time. Also, due to database differencies each method
# ~ of same (but broad) interface would be slightly differnt behavior.
# ~ 
# ~ Also, I really don't want to tight `Sql` object inheritance to the
# ~ actually used engine. It 100% should be late binding. So, nothing
# ~ even close to passing engine instance into table definition Meta
# ~ options.
# ~ 
# ~ The core consept is that we SHOULD NOT OWN `asyncpg.Connection` ~
# ~ instance inside our engine object. Most sertainly would would have
# ~ `Connection` abstract class, a concrete driver adapter for each ~
# ~ supported library.
# ~ 
# ~ ```pycon
# ~ >>> import asyncpg
# ~ >>> import typedsql
# ~ >>> connection = await asyncpg.connect(host='127.0.0.1')
# ~ >>> typedsql.guess_adapter(connection)
# ~ AsyncpgAdapter()
# ~ ```
