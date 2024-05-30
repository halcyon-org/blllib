# TypesGeoJSONPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[object]** |  | 

## Example

```python
from algorithm_lib.models.types_geo_json_point import TypesGeoJSONPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TypesGeoJSONPoint from a JSON string
types_geo_json_point_instance = TypesGeoJSONPoint.from_json(json)
# print the JSON string representation of the object
print(TypesGeoJSONPoint.to_json())

# convert the object into a dict
types_geo_json_point_dict = types_geo_json_point_instance.to_dict()
# create an instance of TypesGeoJSONPoint from a dict
types_geo_json_point_from_dict = TypesGeoJSONPoint.from_dict(types_geo_json_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


