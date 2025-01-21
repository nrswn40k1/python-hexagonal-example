from pytest import fixture

from src.app.port.inbound.i_create_task_usecase import CreateTaskRequest
from src.app.port.outbound.i_task_repository import ITaskRepository
from src.app.usecase.create_task_usecase import CreateTaskUsecase


class TestCreateTaskUsecase:
    @fixture
    def usecase(self, task_repository: ITaskRepository) -> CreateTaskUsecase:
        return CreateTaskUsecase(task_repository)

    def test_run_success(self, usecase: CreateTaskUsecase):
        request = CreateTaskRequest(title="Test task")

        response = usecase.run(request)

        assert response.title == "Test task"
        assert response.status == "todo"
