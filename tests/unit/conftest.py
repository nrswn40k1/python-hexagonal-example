from pytest import fixture

from src.adapter.outbound.inmemory.inmemory_task_repository import (
    InMemoryTaskRepository,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


@fixture
def task_repository() -> ITaskRepository:
    return InMemoryTaskRepository()
