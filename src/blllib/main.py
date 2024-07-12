import json
import os

import functions_framework
from markupsafe import escape
import openapi_client

#print(dir(openapi_client))
print(dir(openapi_client.models.client_delete200_response))

create = openapi_client.models.client_delete200_response
print(create)


SYSTEM_OS = os.name

if SYSTEM_OS == "nt":
    with open("src\\blllib\\data\\test_call.json") as file:
        test_data = json.load(file)


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    if os.name == "nt":
        request_json = test_data
    else:
        request_json = request.get_json(silent=True)
        request_args = request.args

    if request_json and "name" in request_json:
        name = request_json["name"]
    else:
        name = "World"
    return f"Hello {escape(name)}!"


if __name__ == "__main__":
    if SYSTEM_OS == "nt":
        print(hello_http(test_data))
    else:
        functions_framework.http.hello_http()
