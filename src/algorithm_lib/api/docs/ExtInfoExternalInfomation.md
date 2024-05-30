# ExtInfoExternalInfomation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | [**ExtInfoExtInfoId**](ExtInfoExtInfoId.md) |  | 
**external_name** | **str** |  | 
**external_description** | **str** |  | 
**first_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 
**updated_history** | **List[datetime]** |  | 

## Example

```python
from algorithm_lib.models.ext_info_external_infomation import ExtInfoExternalInfomation

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


