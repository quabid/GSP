import requests
import urllib3
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin


# https://www.youtube.com/results?search_query=wingsuits
# https://youtu.be/-DCkuvC28mE
# https://jsonplaceholder.typicode.com/todos
# https://jsonplaceholder.typicode.com/posts
# https://jsonplaceholder.typicode.com/comments
# https://jsonplaceholder.typicode.com/photos
# https://jsonplaceholder.typicode.com/albums


class WebSearcher:
    def __init__(this, url):
        this.url = url
        this.parsed_url = urlparse(url)
        this.split_url = urlsplit(url)
        this.REQUEST_METHODS = {
            'get': lambda url: requests.get(url),
            'post': lambda url, data: requests.post(url, data=data),
            'put': lambda url, data: requests.put(url, data=data),
            'delete': lambda url: requests.delete("{}/delete".format(url)),
            'head': lambda url: requests.head("{}/get".format(url)),
            'options': lambda url: requests.options("{}/get".format(url))
        }

    def get_url(this):
        return this.url

    def make_request(this, method='get', data=None):
        req = this.REQUEST_METHODS[method]
        try:
            if method == 'get':
                return {'status': True, 'data': req(this.url)}
            elif method == 'delete':
                return {'status': True, 'data': req(this.url)}
            elif method == 'head':
                return {'status': True, 'data': req(this.url)}
            elif method == 'options':
                return {'status': True, 'data': req(this.url)}
            else:
                return {'status': True, 'data': req(this.url, data)}
        except requests.exceptions.MissingSchema as ms:
            print(ms)
            return {'error': ms, 'status': False}
        except requests.exceptions.InvalidURL as iu:
            print(iu)
            return {'error': iu, 'status': False}
        except requests.exceptions.InvalidSchema as ins:
            print(ins)
            return {'error': ins, 'status': False}
        except requests.exceptions.ConnectionError as ce:
            print(ce)
            return {'error': ce, 'status': False}
        except urllib3.exceptions.NewConnectionError as nce:
            print(nce)
            return {'error': nce, 'status': False}

    def display(this):
        if this.url != None:
            print("\n\tURL:\t\t{}".format(this.parsed_url.geturl()))
            print("\n\tParsed URL:\t\t{}".format(this.parsed_url))
            if this.parsed_url.port:
                print("\n\tPort:\t\t{}".format(this.parsed_url.port))
            if this.parsed_url[1]:
                pnet_loc = this.parsed_url[1]
                print("\tParse net_loc:\t{}".format(pnet_loc))

            print("\n\tURL:\t\t{}".format(this.split_url.geturl()))
            print("\n\tSplitted URL:\t\t{}".format(this.split_url))
            if this.split_url.port:
                print("\n\tPort:\t\t{}".format(this.split_url.port))
            if this.split_url[1]:
                snet_loc = this.split_url[1]
                print("\tSplit net_loc:\t{}".format(snet_loc))
