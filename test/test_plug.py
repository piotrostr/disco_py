import pytest
from discum import Plug


def test_plug_works():
    plug = Plug()
    assert plug.api_key
    assert plug.url
    res = plug.hello()
    assert res == "eyo"


def test_plug_gets_and_returns_users():
    plug = Plug()
    user = plug.get_user()
    assert user
    assert user["token"]
    res_code = plug.return_user(user)
    assert res_code == 201
