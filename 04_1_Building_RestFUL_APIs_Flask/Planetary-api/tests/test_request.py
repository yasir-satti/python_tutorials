import uuid

import requests

URL = 'https://todo.pixegami.io/'

HTTP_SUCCEEDED = 200
HTTP_NOT_FOUND = 404


def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == HTTP_SUCCEEDED

    data = create_task_response.json()
    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == HTTP_SUCCEEDED

    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == HTTP_SUCCEEDED
    task_id = create_task_response.json()['task']['task_id']

    new_playload = {
        "content": "My create task content",
        "user_id": payload['user_id'],
        "task_id": task_id,
        "is_done": True
    }
    update_task_response = update_task(new_playload)
    assert update_task_response.status_code == HTTP_SUCCEEDED

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == HTTP_SUCCEEDED
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_playload['content']
    assert get_task_data['is_done'] == new_playload['is_done']


def test_can_list_tasks():
    # create a number of tasks for a user
    payload = new_task_payload()
    number_of_tasks = 3
    for _ in range(number_of_tasks):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == HTTP_SUCCEEDED
    # get tasks list for the user
    user_id = payload['user_id']
    list_tasks_response = list_tasks_by_user_id(user_id)
    assert list_tasks_response.status_code == HTTP_SUCCEEDED
    tasks = list_tasks_response.json()['tasks']
    assert len(tasks) == number_of_tasks


def test_can_delete_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == HTTP_SUCCEEDED
    task_id = create_task_response.json()['task']['task_id']
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == HTTP_SUCCEEDED
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == HTTP_NOT_FOUND


def new_task_payload():
    user_id = f'test_user_{uuid.uuid4().hex}'
    content = f'test_content_{uuid.uuid4().hex}'
    return {
        "content": content,
        "user_id": user_id,
        "task_id": "task_001",
        "is_done": False
    }


def create_task(payload):
    return requests.put(URL + '/create-task', json=payload)


def get_task(task_id):
    return requests.get(URL + f'/get-task/{task_id}')


def update_task(new_payload):
    return requests.put(URL + f'/update-task', json=new_payload)


def list_tasks_by_user_id(user_id):
    return requests.get(URL + f'/list-tasks/{user_id}')


def delete_task(task_id):
    return requests.delete(URL + f'/delete-task/{task_id}')
