import uvicorn
from fastapi import FastAPI, HTTPException

from src.app.port.inbound.i_create_task_usecase import (
    CreateTaskRequest,
    CreateTaskResponse,
    FailedToCreateTask,
    ICreateTaskUsecase,
)
from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    FailedToDeleteTask,
    IDeleteTaskUsecase,
)
from src.app.port.inbound.i_progress_status_usecase import (
    FailedToProgressStatus,
    IProgressStatusUsecase,
    ProgressStatusRequest,
    ProgressStatusResponse,
)
from src.app.port.inbound.i_show_tasks_usecase import (
    FailedToShowTasks,
    IShowTasksUsecase,
    ShowTasksResponse,
)

app = FastAPI()


class FastAPIController:
    def __init__(
        self,
        create_task_usecase: ICreateTaskUsecase,
        show_tasks_usecase: IShowTasksUsecase,
        progress_status_usecase: IProgressStatusUsecase,
        delete_task_usecase: IDeleteTaskUsecase,
        port: int = 8000,
        host: str = "0.0.0.0",
    ):
        self.port = port
        self.host = host

        self.create_task_usecase = create_task_usecase
        self.show_tasks_usecase = show_tasks_usecase
        self.progress_status_usecase = progress_status_usecase
        self.delete_task_usecase = delete_task_usecase

        self.create_endpoints(app)

    def run(self):
        uvicorn.run(app, host=self.host, port=self.port)

    def create_endpoints(self, app: FastAPI):
        @app.post("/tasks", response_model=CreateTaskResponse)
        def create_task(request: CreateTaskRequest):
            try:
                response = self.create_task_usecase.run(request)
                return response
            except FailedToCreateTask as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.get("/tasks", response_model=ShowTasksResponse)
        def show_tasks() -> ShowTasksResponse:
            try:
                response = self.show_tasks_usecase.run()
                return response
            except FailedToShowTasks as e:
                raise HTTPException(status_code=500, detail=str(e))

        @app.patch("/tasks/progress/{task_id}", response_model=ProgressStatusResponse)
        def progress_status(task_id: str):
            request = ProgressStatusRequest(task_id=task_id)

            try:
                response = self.progress_status_usecase.run(request)
                return response
            except FailedToProgressStatus as e:
                if e.error_type == "task_not_found":
                    raise HTTPException(status_code=404, detail=str(e))
                raise HTTPException(status_code=500, detail=str(e))

        @app.delete("/tasks/{task_id}", status_code=204)
        def delete_task(task_id: str):
            request = DeleteTaskRequest(task_id=task_id)

            try:
                self.delete_task_usecase.run(request)
            except FailedToDeleteTask as e:
                if e.error_type == "task_not_found":
                    raise HTTPException(status_code=404, detail=str(e))
                raise HTTPException(status_code=500, detail=str(e))
