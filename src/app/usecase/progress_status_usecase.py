from src.app.domain.exceptions import TaskNotFoundException
from src.app.port.inbound.i_progress_status_usecase import (
    FailedToProgressStatus,
    IProgressStatusUsecase,
    ProgressStatusRequest,
    ProgressStatusResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class ProgressStatusUsecase(IProgressStatusUsecase):
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def run(
        self, request: ProgressStatusRequest
    ) -> ProgressStatusResponse | FailedToProgressStatus:
        try:
            return self._run(request)
        except TaskNotFoundException as e:
            return FailedToProgressStatus(error_type="task_not_found", error_msg=str(e))
        except Exception as e:
            return FailedToProgressStatus(error_type="unknown", error_msg=str(e))

    def _run(self, request: ProgressStatusRequest) -> ProgressStatusResponse:
        task = self.task_repository.load_by_id(request.task_id)
        task.progress_status()
        self.task_repository.update(task)
        return ProgressStatusResponse(task=task)
