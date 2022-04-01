import os
import requests


def get_proxy_details():
    proxy_auth = f"{os.environ.get('ZYTE_KEY')}:"
    proxy_host = "proxy.zyte.com"
    proxy_port = 8011
    proxy_type = "http"
    return proxy_type, proxy_auth, proxy_host, proxy_port


def use_zyte_proxy(session: requests.Session):
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

    session.verify = "zyte-smartproxy-ca.crt"
    return session
