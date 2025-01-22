from src.app.domain.task import Task, TaskStatus


def test_task_creation_succeeds():
    task = Task.create(title="Test task")
    assert task.title == "Test task"
    assert task.status == TaskStatus.TODO


def test_task_status_has_been_progressed():
    task = Task.create(title="Test task")
    task.progress_status()
    assert task.status == TaskStatus.IN_PROGRESS

    task.progress_status()
    assert task.status == TaskStatus.DONE

    task.progress_status()
    assert task.status == TaskStatus.DONE
