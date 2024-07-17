# KoyoKoyoData

The data is the result of processing by the koyo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**koyo_data_id** | **str** |  | 
**koyo_id** | **str** | The ID of the koyo that generated the data. | 
**version** | **str** | The version of the koyo used to generate the data. | 
**koyo_scale** | **float** | The resolution of the data. | 
**content_type** | [**KoyoDataType**](KoyoDataType.md) | The type of data format.(enum: image, csv, json...) | 
**content** | **bytearray** | The data content itself. | 
**entry_at** | **datetime** |  | 
**target_at** | **datetime** | The time at which the data is targeted. The time at which data processing began (&#x3D; the primary data from which the data was processed was updated). In other words, it indicates which time the data is based on.\&quot;) | 

## Example

```python
from openapi_client.models.koyo_koyo_data import KoyoKoyoData

# TODO update the JSON string below
json = "{}"
# create an instance of KoyoKoyoData from a JSON string
koyo_koyo_data_instance = KoyoKoyoData.from_json(json)
# print the JSON string representation of the object
print(KoyoKoyoData.to_json())

# convert the object into a dict
koyo_koyo_data_dict = koyo_koyo_data_instance.to_dict()
# create an instance of KoyoKoyoData from a dict
koyo_koyo_data_from_dict = KoyoKoyoData.from_dict(koyo_koyo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


