# ExtInfoCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extinfo** | [**ExtInfoExternalInfomationCreate**](ExtInfoExternalInfomationCreate.md) |  | 

## Example

```python
from openapi_client.models.ext_info_create_request import ExtInfoCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtInfoCreateRequest from a JSON string
ext_info_create_request_instance = ExtInfoCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExtInfoCreateRequest.to_json())

# convert the object into a dict
ext_info_create_request_dict = ext_info_create_request_instance.to_dict()
# create an instance of ExtInfoCreateRequest from a dict
ext_info_create_request_from_dict = ExtInfoCreateRequest.from_dict(ext_info_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


