from pytest import fixture

from src.app.domain.task import Task
from src.app.port.inbound.i_progress_status_usecase import (
    IProgressStatusUsecase,
    ProgressStatusRequest,
    ProgressStatusResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository
from src.app.usecase.progress_status_usecase import ProgressStatusUsecase


class TestProgressStatusUsecase:
    @fixture
    def usecase(self, task_repository: ITaskRepository) -> IProgressStatusUsecase:
        return ProgressStatusUsecase(task_repository)

    def test_run_success(
        self, usecase: IProgressStatusUsecase, existing_tasks: list[Task]
    ):
        task = existing_tasks[0]
        request = ProgressStatusRequest(task_id=task.id)

        response = usecase.run(request)

        assert response == ProgressStatusResponse(
            id=task.id, status="in_progress", title=task.title
        )
