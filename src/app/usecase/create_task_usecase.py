from src.app.domain.task import Task
from src.app.port.inbound.i_create_task_usecase import (
    CreateTaskRequest,
    CreateTaskResponse,
    FailedToCreateTask,
    ICreateTaskUsecase,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class CreateTaskUsecase(ICreateTaskUsecase):
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def run(
        self, request: CreateTaskRequest
    ) -> CreateTaskResponse | FailedToCreateTask:
        try:
            return self._run(request)
        except Exception as e:
            return FailedToCreateTask(error_type="unknown", error_msg=str(e))

    def _run(self, request: CreateTaskRequest) -> CreateTaskResponse:
        task = Task.create(title=request.title)
        self.task_repository.add(task)
        return CreateTaskResponse.create(task)
