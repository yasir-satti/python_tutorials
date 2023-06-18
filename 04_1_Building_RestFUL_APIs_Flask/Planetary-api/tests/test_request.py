import requests

URL = 'https://todo.pixegami.io/'

HTTP_SUCCEEDED = 200


def test_call_endpoint():
    response = requests.get(URL)
    assert response.status_code == HTTP_SUCCEEDED


def test_can_create_task():
    payload = {
        "content": "My create task content",
        "user_id": "user 0",
        "task_id": "task_001",
        "is_done": False
    }
    create_task_response = requests.put(URL + '/create-task', json=payload)
    assert create_task_response.status_code == HTTP_SUCCEEDED

    data = create_task_response.json()
    task_id = data['task']['task_id']
    get_task_response = requests.get(URL + f'/get-task/{task_id}')
    assert get_task_response.status_code == HTTP_SUCCEEDED

    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


