from pytest import fixture

from src.app.domain.task import Task
from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    DeleteTaskResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository
from src.app.usecase.delete_task_usecase import DeleteTaskUsecase


class TestDeleteTaskUsecase:
    @fixture
    def usecase(self, task_repository: ITaskRepository) -> DeleteTaskUsecase:
        return DeleteTaskUsecase(task_repository)

    def test_run_success(self, usecase: DeleteTaskUsecase, existing_tasks: list[Task]):
        task = existing_tasks[0]
        request = DeleteTaskRequest(task_id=task.id)

        response = usecase.run(request)

        assert response == DeleteTaskResponse(success=True)
