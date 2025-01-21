from pytest import fixture

from src.adapter.outbound.inmemory.inmemory_task_repository import (
    InMemoryTaskRepository,
)
from src.app.domain.task import Task
from src.app.port.outbound.i_task_repository import ITaskRepository


@fixture
def existing_tasks() -> list[Task]:
    return [Task.create(title="sample task 1")]


@fixture
def task_repository(existing_tasks) -> ITaskRepository:
    repository = InMemoryTaskRepository()
    for task in existing_tasks:
        repository.add(task)
    return repository
