import pytest
import allure
import requests

#pip install pytest allure requests



@allure.title("TC#1 - Verify creation of token")
@allure.description("Verify create token is working")
@pytest.mark.crud
def get_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"

    full_url = base_url+base_path
    headers = {
            "Content-Type" : "application/json"
    }
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=full_url,headers=headers, json = payload)

    #status code verification
    assert response.status_code == 200
    response_data_json = response.json()
    token = response_data_json["token"]
    assert type(token) == str
    assert len(token) > 1
    return token


@allure.title("TC#1 - Create Booking ID ")
@allure.description("Verify create Booking")
@pytest.mark.crud
def get_bookingid():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"

    full_url = base_url+base_path
    headers = {
            "Content-Type" : "application/json"
    }
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response_data = requests.post(url=full_url,headers=headers, json = payload)\

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_request():
    token = get_token()
    bookingid = get_bookingid()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Pramod"


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201






