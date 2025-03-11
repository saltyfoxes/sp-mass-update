import requests

from tokens import TOKEN 

def get_response(method, url, body = None):
    response = requests.request(method, url, json=body, headers={"Authorization": TOKEN})
    if not response.ok:
        print(response.text)
        response.raise_for_status()
    return response

#create json files
def write_to_file(name, data):
    with open(name, "wb") as file:
         file.write(data)

