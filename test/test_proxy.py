import pytest
import requests

from discum import Client, Plug

from discum.proxy import use_zyte_proxy


@pytest.fixture()
def user():
    plug = Plug()
    user = plug.get_user()
    yield user
    plug.return_user(user)


def test_proxy_works():
    session = requests.Session()
    local_ip = session.get("https://httpbin.org/ip").json()["origin"]
    proxy_session = use_zyte_proxy(session)
    proxy_ip = proxy_session.get("https://httpbin.org/ip").json()["origin"]
    assert local_ip != proxy_ip


def test_proxy_works_on_client(user):
    session = requests.Session()
    local_ip = session.get("https://httpbin.org/ip").json()["origin"]
    client = Client(email=user["email"], password=user["password"], token=user["token"])
    client_ip = client.s.get("https://httpbin.org/ip").json()["origin"]
    assert client_ip != local_ip


@pytest.mark.skip(reason="not implemented yet")
def test_proxy_is_persistant(user):
    pass
