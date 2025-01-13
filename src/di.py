from typing import Union

from src.adapter.inbound.cli.cli_controller import CliController
from src.adapter.inbound.fastapi.fastapi_controller import FastAPIController
from src.app.port.inbound.i_create_task_usecase import ICreateTaskUsecase
from src.app.port.inbound.i_delete_task_usecase import IDeleteTaskUsecase
from src.app.port.inbound.i_progress_status_usecase import IProgressStatusUsecase
from src.app.port.inbound.i_show_tasks_usecase import IShowTasksUsecase
from src.app.port.outbound.i_task_repository import ITaskRepository

Controller = Union[CliController | FastAPIController]


def create_controller() -> Controller:
    from src.config import CONTROLLER_TYPE

    usecases = create_usecases()

    if CONTROLLER_TYPE == "cli":
        return CliController(*usecases)
    elif CONTROLLER_TYPE == "fastapi":
        from src.config import HOST, PORT

        return FastAPIController(*usecases, port=PORT, host=HOST)
    else:
        raise ValueError(f"Invalid CONTROLLER_TYPE: {CONTROLLER_TYPE}")


def create_task_repository() -> ITaskRepository:
    from src.config import TASK_REPOSITORY_TYPE

    if TASK_REPOSITORY_TYPE == "inmemory":
        from src.adapter.outbound.task_repository.inmemory_task_repository import (
            InMemoryTaskRepository,
        )

        return InMemoryTaskRepository()
    else:
        raise ValueError(f"Invalid TASK_REPOSITORY_TYPE: {TASK_REPOSITORY_TYPE}")


def create_usecases() -> (
    tuple[
        ICreateTaskUsecase,
        IShowTasksUsecase,
        IProgressStatusUsecase,
        IDeleteTaskUsecase,
    ]
):
    from src.app.usecase.create_task_usecase import CreateTaskUsecase
    from src.app.usecase.delete_task_usecase import DeleteTaskUsecase
    from src.app.usecase.progress_status_usecase import ProgressStatusUsecase
    from src.app.usecase.show_tasks_usecase import ShowTasksUsecase

    task_repository = create_task_repository()

    create_task_usecase = CreateTaskUsecase(task_repository)
    show_tasks_usecase = ShowTasksUsecase(task_repository)
    update_status_usecase = ProgressStatusUsecase(task_repository)
    delete_task_usecase = DeleteTaskUsecase(task_repository)

    return (
        create_task_usecase,
        show_tasks_usecase,
        update_status_usecase,
        delete_task_usecase,
    )
