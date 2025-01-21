from pytest import fixture

from src.app.domain.task import Task
from src.app.port.inbound.i_show_tasks_usecase import IShowTasksUsecase
from src.app.port.outbound.i_task_repository import ITaskRepository
from src.app.usecase.show_tasks_usecase import ShowTasksUsecase


class TestShowTasksUsecase:
    @fixture
    def usecase(self, task_repository: ITaskRepository) -> IShowTasksUsecase:
        return ShowTasksUsecase(task_repository)

    def test_run_success(self, usecase: IShowTasksUsecase, existing_tasks: list[Task]):
        response = usecase.run()

        assert len(response.tasks) == len(existing_tasks)
        assert all(
            response.tasks[i].id == existing_tasks[i].id
            and response.tasks[i].title == existing_tasks[i].title
            and response.tasks[i].status == existing_tasks[i].status.value
            for i in range(len(existing_tasks))
        )
