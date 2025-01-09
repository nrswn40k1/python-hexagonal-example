from src.app.port.inbound.i_create_task_usecase import (
    CreateTaskRequest,
    ICreateTaskUsecase,
)
from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    IDeleteTaskUsecase,
)
from src.app.port.inbound.i_progress_status_usecase import (
    IProgressStatusUsecase,
    ProgressStatusRequest,
)
from src.app.port.inbound.i_show_tasks_usecase import IShowTasksUsecase


class CliController:
    def __init__(
        self,
        create_task_usecase: ICreateTaskUsecase,
        show_tasks_usecase: IShowTasksUsecase,
        update_status_usecase: IProgressStatusUsecase,
        delete_task_usecase: IDeleteTaskUsecase,
    ):
        self._create_task_usecase = create_task_usecase
        self._show_tasks_usecase = show_tasks_usecase
        self._update_status_usecase = update_status_usecase
        self._delete_task_usecase = delete_task_usecase

    def run(self):
        while True:
            print("------ Options ------")
            print("1. Create Task")
            print("2. Show Tasks")
            print("3. Progress Task Status")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.progress_status()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

    def create_task(self) -> None:
        title = input("Enter task title: ")
        request = CreateTaskRequest(title=title)

        response = self._create_task_usecase.run(request)

        print("Task created successfully!")
        print(response.task.model_dump())

    def show_tasks(self) -> None:
        print("------ Tasks ------")

        response = self._show_tasks_usecase.run()
        for task in response.tasks:
            print(task.model_dump(), end="\n---\n")

    def progress_status(self) -> None:
        task_id = input("Enter task id: ")
        request = ProgressStatusRequest(task_id=task_id)
        response = self._update_status_usecase.run(request)
        print("Task status updated successfully!")
        print(response.task.model_dump())

    def delete_task(self) -> None:
        task_id = input("Enter deleted task_id: ")
        request = DeleteTaskRequest(task_id=task_id)
        self._delete_task_usecase.run(request)
        print("Task deleted successfully!")
