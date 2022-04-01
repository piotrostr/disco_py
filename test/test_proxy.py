import pytest
import requests

from discum import Client, Plug


@pytest.fixture()
def user():
    plug = Plug()
    user = plug.get_user()
    yield user
    plug.return_user(user)


def test_proxy(user):
    my_ip = requests.get("https://httpbin.org/get").json()["origin"]
    client = Client(email=user["email"], password=user["password"], token=user["token"])
    client_ip = client.s.get("https://httpbin.org/get").json()["origin"]
    assert my_ip != client_ip
