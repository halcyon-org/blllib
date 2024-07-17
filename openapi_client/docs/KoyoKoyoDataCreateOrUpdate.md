# KoyoKoyoDataCreateOrUpdate

The data is the result of processing by the koyo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**koyo_id** | **str** | The ID of the koyo that generated the data. | 
**version** | **str** | The version of the koyo used to generate the data. | 
**koyo_scale** | **float** | The resolution of the data. | 
**content_type** | [**KoyoDataType**](KoyoDataType.md) | The type of data format.(enum: image, csv, json...) | 
**content** | **bytearray** | The data content itself. | 

## Example

```python
from openapi_client.models.koyo_koyo_data_create_or_update import KoyoKoyoDataCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KoyoKoyoDataCreateOrUpdate from a JSON string
koyo_koyo_data_create_or_update_instance = KoyoKoyoDataCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print(KoyoKoyoDataCreateOrUpdate.to_json())

# convert the object into a dict
koyo_koyo_data_create_or_update_dict = koyo_koyo_data_create_or_update_instance.to_dict()
# create an instance of KoyoKoyoDataCreateOrUpdate from a dict
koyo_koyo_data_create_or_update_from_dict = KoyoKoyoDataCreateOrUpdate.from_dict(koyo_koyo_data_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


