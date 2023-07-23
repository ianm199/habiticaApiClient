from typing import List, Dict, Optional, Union
from src.client import HabiticaBaseClient


class HabiticaTaskClient(HabiticaBaseClient):
    def get_user_tasks(self, task_type: str = None, due_date: str = None) -> Dict:
        params = {}
        if task_type:
            params['type'] = task_type
        if due_date:
            params['dueDate'] = due_date

        return self.make_request('GET', '/tasks/user', params=params)

    def add_tag_to_task(self, task_id: str, tag_id: str) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/tags/{tag_id}')

    def add_checklist_item(self, task_id: str, text: str, completed: bool = False) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/checklist', data={"text": text, "completed": completed})

    def create_challenge_task(self,
                              challenge_id: str,
                              text: str,
                              task_type: str,
                              attribute: Optional[str] = None,
                              collapse_checklist: Optional[bool] = None,
                              notes: Optional[str] = None,
                              date: Optional[str] = None,
                              priority: Optional[float] = None,
                              reminders: Optional[List[Dict[str, str]]] = None,
                              frequency: Optional[str] = None,
                              repeat: Optional[str] = None,
                              every_x: Optional[int] = None,
                              streak: Optional[int] = None,
                              days_of_month: Optional[List[int]] = None,
                              weeks_of_month: Optional[List[int]] = None,
                              start_date: Optional[str] = None,
                              up: Optional[bool] = None,
                              down: Optional[bool] = None,
                              value: Optional[float] = None) -> Dict:
        """Create a new task belonging to a challenge"""
        task_details = {
            "text": text,
            "type": task_type,
            "attribute": attribute,
            "collapseChecklist": collapse_checklist,
            "notes": notes,
            "date": date,
            "priority": priority,
            "reminders": reminders,
            "frequency": frequency,
            "repeat": repeat,
            "everyX": every_x,
            "streak": streak,
            "daysOfMonth": days_of_month,
            "weeksOfMonth": weeks_of_month,
            "startDate": start_date,
            "up": up,
            "down": down,
            "value": value
        }
        return self.make_request('POST', f'/tasks/challenge/{challenge_id}', data=task_details)

    def create_group_task(self,
                          group_id: str,
                          text: str,
                          task_type: str,
                          attribute: Optional[str] = None,
                          collapse_checklist: Optional[bool] = None,
                          notes: Optional[str] = None,
                          date: Optional[str] = None,
                          priority: Optional[float] = None,
                          reminders: Optional[List[Dict[str, str]]] = None,
                          frequency: Optional[str] = None,
                          repeat: Optional[str] = None,
                          every_x: Optional[int] = None,
                          streak: Optional[int] = None,
                          days_of_month: Optional[List[int]] = None,
                          weeks_of_month: Optional[List[int]] = None,
                          start_date: Optional[str] = None,
                          up: Optional[bool] = None,
                          down: Optional[bool] = None,
                          value: Optional[float] = None) -> Dict:
        """Create a new task belonging to a group"""
        task_details = {
            "text": text,
            "type": task_type,
            "attribute": attribute,
            "collapseChecklist": collapse_checklist,
            "notes": notes,
            "date": date,
            "priority": priority,
            "reminders": reminders,
            "frequency": frequency,
            "repeat": repeat,
            "everyX": every_x,
            "streak": streak,
            "daysOfMonth": days_of_month,
            "weeksOfMonth": weeks_of_month,
            "startDate": start_date,
            "up": up,
            "down": down,
            "value": value
        }
        return self.make_request('POST', f'/tasks/group/{group_id}', data=task_details)

    def create_user_task(self,
                         text: str,
                         task_type: str,
                         tags: Optional[List[str]] = None,
                         alias: Optional[str] = None,
                         attribute: Optional[str] = None,
                         checklist: Optional[List[Dict[str, Union[str, bool]]]] = None,
                         collapse_checklist: Optional[bool] = None,
                         notes: Optional[str] = None,
                         date: Optional[str] = None,
                         priority: Optional[float] = None,
                         reminders: Optional[List[str]] = None,
                         frequency: Optional[str] = None,
                         repeat: Optional[str] = None,
                         every_x: Optional[int] = None,
                         streak: Optional[int] = None,
                         days_of_month: Optional[List[int]] = None,
                         weeks_of_month: Optional[List[int]] = None,
                         start_date: Optional[str] = None,
                         up: Optional[bool] = None,
                         down: Optional[bool] = None,
                         value: Optional[float] = None) -> Dict:
        """Create a new task belonging to the user"""
        task_details = {
            "text": text,
            "type": task_type,
            "tags": tags,
            "alias": alias,
            "attribute": attribute,
            "checklist": checklist,
            "collapseChecklist": collapse_checklist,
            "notes": notes,
            "date": date,
            "priority": priority,
            "reminders": reminders,
            "frequency": frequency,
            "repeat": repeat,
            "everyX": every_x,
            "streak": streak,
            "daysOfMonth": days_of_month,
            "weeksOfMonth": weeks_of_month,
            "startDate": start_date,
            "up": up,
            "down": down,
            "value": value
        }
        return self.make_request('POST', '/tasks/user', data=task_details)

    def delete_task(self, task_id: str) -> Dict:
        """Deletes a task from the user's task list."""
        return self.make_request('DELETE', f'/tasks/{task_id}')

    def update_task(self,
                    task_id: str,
                    text: Optional[str] = None,
                    notes: Optional[str] = None,
                    date: Optional[str] = None,
                    priority: Optional[float] = None,
                    attribute: Optional[str] = None,
                    tags: Optional[List[str]] = None,
                    collapse_checklist: Optional[bool] = None,
                    reminders: Optional[List[Dict[str, str]]] = None,
                    frequency: Optional[str] = None,
                    every_x: Optional[int] = None,
                    streak: Optional[int] = None,
                    days_of_month: Optional[List[int]] = None,
                    weeks_of_month: Optional[List[int]] = None,
                    start_date: Optional[str] = None,
                    up: Optional[bool] = None,
                    down: Optional[bool] = None,
                    value: Optional[float] = None) -> Dict:
        """Updates a task's details."""
        task_details = {
            "text": text,
            "notes": notes,
            "date": date,
            "priority": priority,
            "attribute": attribute,
            "tags": tags,
            "collapseChecklist": collapse_checklist,
            "reminders": reminders,
            "frequency": frequency,
            "everyX": every_x,
            "streak": streak,
            "daysOfMonth": days_of_month,
            "weeksOfMonth": weeks_of_month,
            "startDate": start_date,
            "up": up,
            "down": down,
            "value": value
        }
        return self.make_request('PUT', f'/tasks/{task_id}', data=task_details)

    def score_task(self, task_id: str, direction: str) -> Dict:
        """Scores a task."""
        return self.make_request('POST', f'/tasks/{task_id}/score/{direction}')


    def move_group_task(self, group_id: str, task_id: str, position: int) -> Dict:
        return self.make_request('POST', f'/group/{group_id}/tasks/{task_id}/move/to/{position}')

    def move_task(self, task_id: str, position: int) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/move/to/{position}')

    def require_more_work_for_task(self, task_id: str, user_id: str) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/needs-work/{user_id}')

    def score_checklist_item(self, task_id: str, item_id: str) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/checklist/{item_id}/score')

    def unassign_user_from_task(self, task_id: str, assigned_user_id: str) -> Dict:
        return self.make_request('POST', f'/tasks/{task_id}/unassign/{assigned_user_id}')

    def unlink_challenge_task(self, task_id: str, keep: str) -> Dict:
        return self.make_request('POST', f'/tasks/unlink-one/{task_id}', query_params={"keep": keep})

    def unlink_all_tasks_from_challenge(self, challenge_id: str, keep: str) -> Dict:
        return self.make_request('POST', f'/tasks/unlink-all/{challenge_id}', query_params={"keep": keep})

    def update_checklist_item(self, task_id: str, item_id: str, text: str, completed: bool) -> Dict:
        body = {
            "text": text,
            "completed": completed
        }
        return self.make_request('PUT', f'/tasks/{task_id}/checklist/{item_id}', body=body)



if __name__ == '__main__':
    print("test!")