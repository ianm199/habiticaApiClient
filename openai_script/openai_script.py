import os
import openai
from concurrent.futures import ProcessPoolExecutor
from collections import defaultdict
from open_ai_schema import Output

DEFAULT_MODEL = "gpt-3.5-turbo"
LARGE_WINDOW_GPT3 = "gpt-3.5-turbo-16k"
GPT_4 = "gpt-4"
LARGE_WINDOW_GPT4 = "gpt-4-32k"

def create_api_client_tests(threaded: bool = False) -> None:
    prompt = """
    Only responde with code as plain text, without code block syntax around it. Include the relevant import statements,
    Include no other text in your response. Your job is to look at sections of the HabiticaAPIClient and create test cases
    for them. In situations where your asked for an "id" fo some sort like task_id, but you don't understand what to do, 
    leave a comment indicating that. Use thios test file for reference:
    ```
    import os
import unittest
from src.tasks import HabiticaTaskClient

class TestHabiticaTaskClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.task_client = HabiticaTaskClient(user_id, api_key)
        self.dummy_task = self.task_client.create_user_task("Dummy Data", task_type="todo")

    def test_get_user_tasks(self):
        response = self.task_client.get_user_tasks()
        self.assertTrue(response, list)

    def test_create_user_task(self):
        daily_user_task = self.task_client.create_user_task("Example daily", task_type="todo")
        self.assertEqual(daily_user_task['text'],"Example daily")
        self.assertEqual(daily_user_task['type'],"todo")

    def test_add_checklist_item_and_score_update(self):
        checklist_item = self.task_client.add_checklist_item(task_id=self.dummy_task['id'], text="test checklist", completed="false")
        self.assertTrue(checklist_item['checklist'][0]['text'], "test checklist")
        score_checklist = self.task_client.score_checklist_item(task_id=self.dummy_task['id'], item_id=checklist_item['checklist'][0]['id'])
        self.assertIsInstance(score_checklist, dict)
        update_checklist_item = self.task_client.update_checklist_item(self.dummy_task['id'], checklist_item['checklist'][0]['id'], text="update", completed=False)
        self.assertEqual(update_checklist_item['checklist'][0]['text'], "update")
    ```
    Here is the file you are making tests for:
    {}
    """
    path_to_test_folder = "../tests"
    path_to_src_files = "../src"
    if threaded:
        with ProcessPoolExecutor() as processor:
            for file in os.listdir(path_to_src_files):
                file_object = file.split("/")[-1].rstrip(".py")
                file_contents = str(open(file).read())
                processor.submit(write_client_file, file_object, "../test", file_contents, prompt, DEFAULT_MODEL)
    else:
        for file in os.listdir(path_to_src_files):
            file_object = file.rstrip(".py")
            file_contents = str(open(os.path.join(path_to_src_files, file)).read())
            write_client_file(file_object, "../test", file_contents, prompt, DEFAULT_MODEL)


def create_main_api_client(threaded: bool = False) -> None:
    api_schema_dict = get_content_dict("apiSchema.txt")
    prompt = """
    Only respond with code as plain text, without code block syntax around it. Include the relevant import statements.
     Include no other text in your response. Your job is to 
    look at these endpoint schemas from the Habitica open source project and create a Python class Habitica<ObjectType>Client
    where <ObjectType> is the type of objcet. I.e. for tasks it is HabiticaTaskClient, for challenge, it is HabiticaChallengeClient 
    that extends the Habitica base class HabiticaBaseClient. Import it with from client import HabiticaBaseClient. These schema are in ApiDoc format.
    Schema:
    {}
    HabiticaBaseClient for reference:
    class HabiticaBaseClient:
        def __init__(self, api_user: str, api_key: str, base_url: str = 'https://habitica.com/api/v3'):
            self.api_user = api_user
            self.api_key = api_key
            self.base_url = base_url

        def make_request(self, method: str, endpoint: str, params: Optional[dict] = None, data: Optional[dict] = None) -> Dict:
            url = f"{{self.base_url}}{{endpoint}}"
            headers = {{'x-api-user': self.api_user, 'x-api-key': self.api_key}}
            if data:
                request_data = {{}}
                for key, val in data.items():
                    if type(val) == bool:
                        request_data[key] = str(val).lower()
                    elif val is not None:
                        request_data[key] = val
            if method == "POST" and data:
                response = requests.request(method, url, headers=headers, data=request_data)
            else:
                extra_args = {{}}
                if params:
                    extra_args["params"] = params
                if data:
                    extra_args["data"] = request_data
                response = requests.request(method, url, headers=headers, **extra_args)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(f"Response Json:")
                print(response.json())
                raise e
            return response.json()['data']

    HabiticaTaskClient for reference:
    class HabiticaTaskClient(HabiticaBaseClient):
        def get_user_tasks(self, task_type: str = None, due_date: str = None) -> Dict:
            params = {{}}
            if task_type:
                params['type'] = task_type
            if due_date:
                params['dueDate'] = due_date

            return self.make_request('GET', '/tasks/user', params=params)

        def add_tag_to_task(self, task_id: str, tag_id: str) -> Dict:
            return self.make_request('POST', f'/tasks/{{task_id}}/tags/{{tag_id}}')

        def add_checklist_item(self, task_id: str, text: str, completed: bool = False) -> Dict:
            return self.make_request('POST', f'/tasks/{{task_id}}/checklist', data={{"text": text, "completed": completed}})

        def create_challenge_task(self,
                                  challenge_id: str,
                                  text: str,
                                  task_type: str,
                                  attribute: Optional[str] = None,
                                  collapse_checklist: Optional[bool] = None,
        """
    if threaded:
        with ProcessPoolExecutor() as processor:
            for object_type, api_docs in api_schema_dict.items():
                processor.submit(write_client_file, object_type, "../src", api_docs, prompt)
    else:
        for object_type, api_docs in api_schema_dict.items():
            write_client_file(object_type, "../src",  api_docs, prompt)

def get_content_dict(schema_file_path: str) -> dict:
    """
    Creates a dict from the ApiSchema.txt file where the keys are the file names and the values are the list of
    lines in order.
    :param schema_file_path:
    :type schema_file_path:
    :return:
    :rtype:
    """
    result = defaultdict(list)
    with open(schema_file_path) as f:
        for line in f:
            if ".js" not in line:
                continue
            line = line.lstrip("./")
            split = line.split(".js")
            filename = split[0] if "/" not in split[0] else split[0].split("/")[1]
            content = split[1:]
            result[filename].extend(content)

    return result

def write_client_file(object_type: str, file_path: str, object_data: str, prompt: str, gpt_model = GPT_4) -> None:
    full_file_path = os.path.join(file_path, f"{object_type}.py")
    if os.path.exists(full_file_path):
        print(f"Skipping {full_file_path} because it already exists")
        return
    full_prompt = prompt.format(object_data)
    token_estimate = len(full_prompt) // 4
    if token_estimate > 4000:
        gpt_model = LARGE_WINDOW_GPT4
    openai_call = openai.ChatCompletion.create(model=gpt_model, messages=[{"role": "user", "content": full_prompt}])
    openai_output = Output.init_from_json(json_dict=openai_call)
    with open(full_file_path, 'w') as f:
        f.write(openai_output.choices[0].message.content)
    print(f"Wrote file: {full_file_path}")


if __name__ == '__main__':
    # create_main_api_client(threaded=True)
    create_api_client_tests(False)