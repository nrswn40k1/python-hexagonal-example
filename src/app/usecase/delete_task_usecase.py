from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    DeleteTaskResponse,
    IDeleteTaskUsecase,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class DeleteTaskUsecase(IDeleteTaskUsecase):
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def run(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        try:
            self.task_repository.delete(task_id=request.task_id)
            return DeleteTaskResponse(result="success")
        except Exception:
            return DeleteTaskResponse(result="failure")
