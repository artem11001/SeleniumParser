import requests
from mod.log import LogFile
from mod import option


log = LogFile(printLog=1)


def get(head: str = option.defaultUserHeader, url: str = '') -> None:
    try:
        p = requests.get(url,  headers=head, timeout=(3, 6))
    except requests.exceptions.ConnectionError as e:
        log(e)
        return 3
    except requests.exceptions.ConnectTimeout as e:
        log(e)
        return 3
    except requests.exceptions.HTTPError as e:
        log(e)
        return 3
    except requests.exceptions.Timeout as e:
        log(e)
        return 3
    if hasattr(p, 'status_code'):
        if(p.status_code == 200):
            return p.text
        else:
            return log('status coke=%s, d=%s' % (p.status_code, p.text))
    else:
        log('not status_code attr url=%s' % url)
        return 3


def post(head: str = option.defaultUserHeader, url: str = '') -> None:
    try:
        p = requests.get(url,  headers=head, timeout=(3, 6))
    except requests.exceptions.ConnectionError as e:
        log(e)
        return 3
    except requests.exceptions.ConnectTimeout as e:
        log(e)
        return 3
    except requests.exceptions.HTTPError as e:
        log(e)
        return 3
    except requests.exceptions.Timeout as e:
        log(e)
        return 3
    if hasattr(p, 'status_code'):
        if(p.status_code == 200):
            return p.content
        else:
            return log('status coke=%s, d=%s' % (p.status_code, p.text))
    else:
        log('not status_code attr url=%s' % url)
        return 3
