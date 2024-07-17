# ExtInfoExternalInfomationCreate

Basic information about the external information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_name** | **str** |  | 
**external_description** | **str** |  | 
**license** | **str** |  | 
**license_description** | **str** |  | 
**first_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 
**updated_history** | **List[datetime]** |  | 

## Example

```python
from openapi_client.models.ext_info_external_infomation_create import ExtInfoExternalInfomationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExtInfoExternalInfomationCreate from a JSON string
ext_info_external_infomation_create_instance = ExtInfoExternalInfomationCreate.from_json(json)
# print the JSON string representation of the object
print(ExtInfoExternalInfomationCreate.to_json())

# convert the object into a dict
ext_info_external_infomation_create_dict = ext_info_external_infomation_create_instance.to_dict()
# create an instance of ExtInfoExternalInfomationCreate from a dict
ext_info_external_infomation_create_from_dict = ExtInfoExternalInfomationCreate.from_dict(ext_info_external_infomation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


