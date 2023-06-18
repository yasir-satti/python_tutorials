import requests

URL = 'http://localhost:5000'

HTTP_SUCCEEDED = 200
HTTP_NOT_AUTHORISED = 401
HTTP_NOT_FOUND = 404


def test_can_call_home_page():
    home_page_response = get_url('/')
    assert home_page_response.status_code == HTTP_SUCCEEDED
    data = home_page_response.json()
    print(data)
    # assert data == 'Hello World!'


def test_can_call_super_simple():
    expected_response = payload('super_simple')
    super_simple_response = get_url('/super_simple')
    assert super_simple_response.status_code == HTTP_SUCCEEDED
    data = super_simple_response.json()
    assert data == expected_response


def test_can_call_url_variables_authorised_age():
    expected_response = payload('url_variables_authorised_age')
    url_variables_response = get_url('/url_variables/Yasir/29')
    assert url_variables_response.status_code == HTTP_SUCCEEDED
    data = url_variables_response.json()
    assert data == expected_response


def test_can_call_url_variables_not_authorised_age():
    expected_response = payload('url_variables_not_authorised_age')
    url_variables_response = get_url('/url_variables/Yasir/16')
    assert url_variables_response.status_code == HTTP_NOT_AUTHORISED
    data = url_variables_response.json()
    assert data == expected_response


def test_can_get_planets_list():
    expected_response = planets()
    planets_list_response = get_url('/planets')
    assert planets_list_response.status_code == HTTP_SUCCEEDED
    assert planets_list_response.json() == expected_response


def get_url(route):
    return requests.get(URL + f'{route}')


def payload(route):
    if route == 'super_simple':
        return {'message': 'Hello from the Planetary API.'}
    elif route == 'url_variables_authorised_age':
        return  {'message': 'Welcome Yasir, you are old enough!'}
    elif route == 'url_variables_not_authorised_age':
        return  {'message': 'Sorry Yasir, you are not old enough.'}
    

def planets():
    return [
    {
        "distance": 1234234534634534.0,
        "home_star": "Sol",
        "mass": 3453454234523.0,
        "planet_id": 1,
        "planet_name": "Mercury",
        "planet_type": "Class Z",
        "radius": 234234.0
    },
    {
        "distance": 92960000.0,
        "home_star": "Sol",
        "mass": 5.972e+24,
        "planet_id": 3,
        "planet_name": "Earth",
        "planet_type": "Class M",
        "radius": 3959.0
    },
    {
        "distance": 12312312.0,
        "home_star": "Sol",
        "mass": 3423423423.0,
        "planet_id": 4,
        "planet_name": "Neptune",
        "planet_type": "Class K",
        "radius": 123123.0
    },
    {
        "distance": 123123121234.0,
        "home_star": "Sol",
        "mass": 342342342323245.0,
        "planet_id": 5,
        "planet_name": "Jupiter",
        "planet_type": "Class K",
        "radius": 123123243.0
    },
    {
        "distance": 123123121234.0,
        "home_star": "Sol",
        "mass": 342342342323245.0,
        "planet_id": 6,
        "planet_name": "Saturn",
        "planet_type": "Class K",
        "radius": 123123243.0
    }
]
