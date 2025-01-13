class TaskNotFoundException(Exception):
    def __init__(self, task_id: str):
        self.task_id = task_id
        self.message = f"Task with id {task_id} not found"
        super().__init__(self.message)
