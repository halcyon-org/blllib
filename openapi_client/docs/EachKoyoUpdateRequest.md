# EachKoyoUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_koyo** | [**KoyoKoyoInfomationCreateOrUpdate**](KoyoKoyoInfomationCreateOrUpdate.md) |  | 

## Example

```python
from openapi_client.models.each_koyo_update_request import EachKoyoUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EachKoyoUpdateRequest from a JSON string
each_koyo_update_request_instance = EachKoyoUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EachKoyoUpdateRequest.to_json())

# convert the object into a dict
each_koyo_update_request_dict = each_koyo_update_request_instance.to_dict()
# create an instance of EachKoyoUpdateRequest from a dict
each_koyo_update_request_from_dict = EachKoyoUpdateRequest.from_dict(each_koyo_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


