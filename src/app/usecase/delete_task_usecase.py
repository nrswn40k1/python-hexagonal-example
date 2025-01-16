from src.app.domain.exceptions import TaskNotFoundException
from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    DeleteTaskResponse,
    FailedToDeleteTask,
    IDeleteTaskUsecase,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class DeleteTaskUsecase(IDeleteTaskUsecase):
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def run(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        try:
            return self._run(request)
        except TaskNotFoundException as e:
            raise FailedToDeleteTask(error_type="task_not_found", error_msg=str(e))
        except Exception as e:
            raise FailedToDeleteTask(error_type="unknown", error_msg=str(e))

    def _run(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        self.task_repository.delete(task_id=request.task_id)
        return DeleteTaskResponse()
