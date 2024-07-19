# KoyoCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**koyo** | [**KoyoKoyoInfomationCreate**](KoyoKoyoInfomationCreate.md) |  | 

## Example

```python
from openapi_client.models.koyo_create_request import KoyoCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KoyoCreateRequest from a JSON string
koyo_create_request_instance = KoyoCreateRequest.from_json(json)
# print the JSON string representation of the object
print(KoyoCreateRequest.to_json())

# convert the object into a dict
koyo_create_request_dict = koyo_create_request_instance.to_dict()
# create an instance of KoyoCreateRequest from a dict
koyo_create_request_from_dict = KoyoCreateRequest.from_dict(koyo_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


