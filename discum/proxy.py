import base64
import os
import requests


def get_proxy_details():
    proxy_auth = f"{os.environ.get('ZYTE_KEY')}:"
    proxy_host = "proxy.zyte.com"
    proxy_port = 8011
    proxy_type = "http"
    return proxy_type, proxy_auth, proxy_host, proxy_port


def get_crawlera_session():
    """
    get a crawlera session
    """
    proxy_auth = f"{os.environ.get('ZYTE_KEY')}:"
    proxy_auth = base64.b64encode(proxy_auth.encode("utf-8"))
    auth_header = "Basic " + proxy_auth.decode("utf-8")
    res = requests.post(
        "http://proxy.zyte.com:8011/sessions",
        headers={"Authorization": auth_header},
        data={},
    )
    return res.text


def use_zyte_proxy(session: requests.Session, user_session: str = None):
    """
    wrapper around requests session to use zyte proxy
    """
    proxy_type, proxy_auth, proxy_host, proxy_port = get_proxy_details()
    session.proxies.update(
        {
            "http": f"{proxy_type}://{proxy_auth}@{proxy_host}:{proxy_port}",
            "https": f"{proxy_type}://{proxy_auth}@{proxy_host}:{proxy_port}",
        }
    )
    session.headers.update(
        {
            "X-Crawlera-Profile": "pass",
            "X-Crawlera-Session": user_session
            if user_session
            else get_crawlera_session(),
        }
    )
    session.verify = "zyte-smartproxy-ca.crt"
    return session
