# KoyoKoyoInfomationCreate

Basic information about the koyo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**koyo_name** | **str** |  | 
**koyo_description** | **str** |  | 
**need_external** | [**List[ExtInfoExtInfoId]**](ExtInfoExtInfoId.md) |  | 
**koyo_params** | **Dict[str, str]** | Koyo parameters. The key is the parameter name and the value is the default value. | 
**koyo_scales** | **List[float]** | Koyo scales is resolution (e.g. one data per meter). Returns a list of supported scales. | 
**koyo_data_ids** | **List[str]** |  | 
**version** | **str** | Semantic versioning | 
**license** | **str** |  | 
**ext_licenses** | **List[str]** | Licenses for primary information and other information used by the koyo. | 

## Example

```python
from openapi_client.models.koyo_koyo_infomation_create import KoyoKoyoInfomationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of KoyoKoyoInfomationCreate from a JSON string
koyo_koyo_infomation_create_instance = KoyoKoyoInfomationCreate.from_json(json)
# print the JSON string representation of the object
print(KoyoKoyoInfomationCreate.to_json())

# convert the object into a dict
koyo_koyo_infomation_create_dict = koyo_koyo_infomation_create_instance.to_dict()
# create an instance of KoyoKoyoInfomationCreate from a dict
koyo_koyo_infomation_create_from_dict = KoyoKoyoInfomationCreate.from_dict(koyo_koyo_infomation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


