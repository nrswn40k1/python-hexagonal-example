from src.app.port.inbound.i_show_tasks_usecase import (
    FailedToShowTasks,
    IShowTasksUsecase,
    ShowTasksResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class ShowTasksUsecase(IShowTasksUsecase):
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def run(self) -> ShowTasksResponse | FailedToShowTasks:
        try:
            return self._run()
        except Exception as e:
            return FailedToShowTasks(error_type="unknown", error_msg=str(e))

    def _run(self) -> ShowTasksResponse:
        tasks = self.task_repository.load_all()
        return ShowTasksResponse.create(tasks=tasks)
