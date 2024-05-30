# ExtInfoCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | [**ExtInfoExtInfoId**](ExtInfoExtInfoId.md) |  | 
**external_name** | **str** |  | 
**external_description** | **str** |  | 
**first_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 
**updated_history** | **List[datetime]** |  | 
**bearer_token** | **str** |  | 

## Example

```python
from algorithm_lib.models.ext_info_create200_response import ExtInfoCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExtInfoCreate200Response from a JSON string
ext_info_create200_response_instance = ExtInfoCreate200Response.from_json(json)
# print the JSON string representation of the object
print(ExtInfoCreate200Response.to_json())

# convert the object into a dict
ext_info_create200_response_dict = ext_info_create200_response_instance.to_dict()
# create an instance of ExtInfoCreate200Response from a dict
ext_info_create200_response_from_dict = ExtInfoCreate200Response.from_dict(ext_info_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


