import os
from src.tasks import HabiticaTaskClient
from datetime import datetime, timedelta

if __name__ == '__main__':
    # Gets last weeks completedToDo's
    today = datetime.today()
    client = HabiticaTaskClient(os.environ.get("HABITICA_USER_ID"), os.environ.get("HABITICA_API_KEY"))
    completed_todos = client.get_user_tasks(task_type="completedTodos")
    completed_this_week = []
    for task in completed_todos:
        if datetime.strptime(task['dateCompleted'], "%Y-%m-%dT%H:%M:%S.%fZ") <= today - timedelta(days=7):
            completed_this_week.append(task)
    print(f"{len(completed_this_week)} completed in past week, not bad")