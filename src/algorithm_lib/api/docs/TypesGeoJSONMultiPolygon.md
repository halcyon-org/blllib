# TypesGeoJSONMultiPolygon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[object]]]** |  | 

## Example

```python
from algorithm_lib.models.types_geo_json_multi_polygon import TypesGeoJSONMultiPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of TypesGeoJSONMultiPolygon from a JSON string
types_geo_json_multi_polygon_instance = TypesGeoJSONMultiPolygon.from_json(json)
# print the JSON string representation of the object
print(TypesGeoJSONMultiPolygon.to_json())

# convert the object into a dict
types_geo_json_multi_polygon_dict = types_geo_json_multi_polygon_instance.to_dict()
# create an instance of TypesGeoJSONMultiPolygon from a dict
types_geo_json_multi_polygon_from_dict = TypesGeoJSONMultiPolygon.from_dict(types_geo_json_multi_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


