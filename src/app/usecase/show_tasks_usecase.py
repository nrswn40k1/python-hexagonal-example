from src.app.port.inbound.i_show_tasks_usecase import (
    IShowTasksUsecase,
    ShowTasksResponse,
)
from src.app.port.outbound.i_task_repository import ITaskRepository


class ShowTasksUsecase(IShowTasksUsecase):
    def __init__(self, task_repository: ITaskRepository) -> None:
        self.task_repository = task_repository

    def run(self) -> ShowTasksResponse:
        tasks = self.task_repository.load_all()
        return ShowTasksResponse(tasks=tasks)
