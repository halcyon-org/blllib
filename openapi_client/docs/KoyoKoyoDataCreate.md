# KoyoKoyoDataCreate

The data is the result of processing by the koyo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the koyo used to generate the data. | 
**koyo_scale** | **float** | The resolution of the data. | 
**content_type** | [**KoyoDataType**](KoyoDataType.md) | The type of data format.(enum: image, csv, json...) | 
**content** | **bytearray** | The data content itself. | 

## Example

```python
from openapi_client.models.koyo_koyo_data_create import KoyoKoyoDataCreate

# TODO update the JSON string below
json = "{}"
# create an instance of KoyoKoyoDataCreate from a JSON string
koyo_koyo_data_create_instance = KoyoKoyoDataCreate.from_json(json)
# print the JSON string representation of the object
print(KoyoKoyoDataCreate.to_json())

# convert the object into a dict
koyo_koyo_data_create_dict = koyo_koyo_data_create_instance.to_dict()
# create an instance of KoyoKoyoDataCreate from a dict
koyo_koyo_data_create_from_dict = KoyoKoyoDataCreate.from_dict(koyo_koyo_data_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


