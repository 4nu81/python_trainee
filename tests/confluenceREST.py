import argparse
import requests
import json
import lxml.etree

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')
    namespace = parser.parse_args()
    return {k:v for k,v in vars(namespace).items() if v}

def get_page(pagename, bereich, user, password):
    base_url = "http://rcs-confluence/rest/api/content"

    params = {
        'title':pagename,
        'expand':'body.view',
        'spaceKey':bereich
    }

    url = ''.join([base_url,'/?','&'.join(['{k}={v}'.format(k=k,v=v) for k,v in params.items()])])

    resp2 = requests.get(url, auth=(user, password))
    response = resp2.json()
    result = []
    for item in response['results']:
        result.append(item['body']['view']['value'])
    return '<hr>'.join(result)

def get_page_by_Id(id, user, password):
    base_url = "http://rcs-confluence/rest/api/content"

    params = {
        'expand':'body.view'
    }

    url = ''.join([base_url,'/',id,'/?','&'.join(['{k}={v}'.format(k=k,v=v) for k,v in params.items()])])

    resp2 = requests.get(url, auth=(user, password))
    return resp2


def replace_img_links(html):
    root = lxml.etree.HTML(html)
    for img in root.iter('img'):
        path = img.get('src', None)
        path = ''.join([base_url,path])
        img.set('src', path)
    return lxml.etree.tostring(root)

command_line_args = get_args()
base_url = 'http://rcs-confluence'

def search_content(searchDict):
    pass



# bei get_page_by_id muss ich hingegen irgendwie die Id ermitteln.
response = get_page_by_Id('6160465', command_line_args['user'], command_line_args['password'])
content = json.loads(response.content)['body']['view']['value']
content = replace_img_links(content)
with open('body2.html', 'w') as f:
    f.write(content)