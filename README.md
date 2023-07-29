## Unofficial API Client For Habitica
This project is an API Client for interacting with the Habitica API. I thought it might be helpful for users, since the
user base tends to be interested in automation anyway. The client is broken down into many sub clients based on the object
type that the user is interacting with. It follows the main pattern of the [Habitica API](https://habitica.com/apidoc/).

### Usage
Example getting list of tasks for your user:
```python
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
    print(f"{len(completed_this_week)} tasks completed in past week, not bad")
```
```commandline
7 tasks completed in past week, not bad
```

### Current state of the project
There is mock tests for just about every method, but they are not fleshed out. Adding integration tests was not really 
realistic given the constraints of many of the API routes and also the number of them, so it's possible not all them 
work as intended. 

### Roadmap
* Add command line tool
* Flesh out tests more
* Add better typing for ease of use

