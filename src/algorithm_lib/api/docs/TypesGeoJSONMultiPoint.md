# TypesGeoJSONMultiPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[object]]** |  | 

## Example

```python
from algorithm_lib.models.types_geo_json_multi_point import TypesGeoJSONMultiPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TypesGeoJSONMultiPoint from a JSON string
types_geo_json_multi_point_instance = TypesGeoJSONMultiPoint.from_json(json)
# print the JSON string representation of the object
print(TypesGeoJSONMultiPoint.to_json())

# convert the object into a dict
types_geo_json_multi_point_dict = types_geo_json_multi_point_instance.to_dict()
# create an instance of TypesGeoJSONMultiPoint from a dict
types_geo_json_multi_point_from_dict = TypesGeoJSONMultiPoint.from_dict(types_geo_json_multi_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


