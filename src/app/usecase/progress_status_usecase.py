from src.app.port.inbound.i_progress_status_usecase import (
    IProgressStatusUsecase,
    ProgressStatusRequest,
    ProgressStatusResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class ProgressStatusUsecase(IProgressStatusUsecase):
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def run(self, request: ProgressStatusRequest) -> ProgressStatusResponse:
        task = self.task_repository.load_by_id(request.task_id)
        task.progress_status()
        self.task_repository.update(task)
        return ProgressStatusResponse(task=task)
