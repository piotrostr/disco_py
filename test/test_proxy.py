import pytest
import requests

from discum import Client, Plug

from discum.proxy import use_zyte_proxy, get_crawlera_session


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


def test_get_crawlera_session():
    session_id = get_crawlera_session()
    assert session_id is not None
    assert isinstance(session_id, str)
    assert len(session_id) > 5


def test_proxy_is_persistant(user):
    client = Client(email=user["email"], password=user["password"], token=user["token"])
    uno = client.s.get("https://httpbin.org/ip").json()["origin"]
    dos = client.s.get("https://httpbin.org/ip").json()["origin"]
    tres = client.s.get("https://httpbin.org/ip").json()["origin"]
    assert uno == dos == tres
