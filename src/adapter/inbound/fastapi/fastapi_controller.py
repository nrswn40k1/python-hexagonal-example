import uvicorn
from fastapi import FastAPI, HTTPException

from src.app.port.inbound.i_create_task_usecase import (
    CreateTaskRequest,
    CreateTaskResponse,
    ICreateTaskUsecase,
)
from src.app.port.inbound.i_delete_task_usecase import (
    DeleteTaskRequest,
    DeleteTaskResponse,
    IDeleteTaskUsecase,
)
from src.app.port.inbound.i_progress_status_usecase import (
    IProgressStatusUsecase,
    ProgressStatusRequest,
    ProgressStatusResponse,
)
from src.app.port.inbound.i_show_tasks_usecase import (
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
            response = self.create_task_usecase.run(request)
            if isinstance(response, CreateTaskResponse):
                return response
            raise HTTPException(status_code=500, detail=response.error_msg)

        @app.get("/tasks", response_model=ShowTasksResponse)
        def show_tasks() -> ShowTasksResponse:
            response = self.show_tasks_usecase.run()
            if isinstance(response, ShowTasksResponse):
                return response
            raise HTTPException(status_code=500, detail=response.error_msg)

        @app.patch("/tasks/progress/{task_id}", response_model=ProgressStatusResponse)
        def progress_status(task_id: str):
            request = ProgressStatusRequest(task_id=task_id)
            response = self.progress_status_usecase.run(request)
            if isinstance(response, ProgressStatusResponse):
                return response
            if response.error_type == "task_not_found":
                raise HTTPException(status_code=404, detail=response.error_msg)
            raise HTTPException(status_code=500, detail=response.error_msg)

        @app.delete("/tasks/{task_id}", status_code=204)
        def delete_task(task_id: str):
            request = DeleteTaskRequest(task_id=task_id)
            response = self.delete_task_usecase.run(request)
            if isinstance(response, DeleteTaskResponse):
                return
            if response.error_type == "task_not_found":
                raise HTTPException(status_code=404, detail=response.error_msg)
            raise HTTPException(status_code=500, detail=response.error_msg)
