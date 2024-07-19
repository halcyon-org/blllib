# ExtInfoExternalInfomation

Basic information about the external information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | [**ExtInfoExtInfoId**](ExtInfoExtInfoId.md) | This ID can be obtained through admin api. It is a human friendly format like GitHub repository names. Only the pattern &#x60;^[a-z_-]{1,64}$&#x60; is allowed. | 
**external_name** | **str** |  | 
**external_description** | **str** |  | 
**license** | **str** |  | 
**license_description** | **str** |  | 
**first_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 
**updated_history** | **List[datetime]** |  | 

## Example

```python
from openapi_client.models.ext_info_external_infomation import ExtInfoExternalInfomation

# TODO update the JSON string below
json = "{}"
# create an instance of ExtInfoExternalInfomation from a JSON string
ext_info_external_infomation_instance = ExtInfoExternalInfomation.from_json(json)
# print the JSON string representation of the object
print(ExtInfoExternalInfomation.to_json())

# convert the object into a dict
ext_info_external_infomation_dict = ext_info_external_infomation_instance.to_dict()
# create an instance of ExtInfoExternalInfomation from a dict
ext_info_external_infomation_from_dict = ExtInfoExternalInfomation.from_dict(ext_info_external_infomation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


