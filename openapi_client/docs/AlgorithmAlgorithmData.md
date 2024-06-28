# AlgorithmAlgorithmData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_id** | **str** |  | 
**version** | **str** | Semantic versioning | 
**algorithm_data_id** | **str** |  | 
**algorithm_scale** | **float** |  | 
**content_type** | [**AlgorithmDataType**](AlgorithmDataType.md) |  | 
**content** | **bytearray** |  | 
**entry_at** | **datetime** |  | 
**target_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.algorithm_algorithm_data import AlgorithmAlgorithmData

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmAlgorithmData from a JSON string
algorithm_algorithm_data_instance = AlgorithmAlgorithmData.from_json(json)
# print the JSON string representation of the object
print(AlgorithmAlgorithmData.to_json())

# convert the object into a dict
algorithm_algorithm_data_dict = algorithm_algorithm_data_instance.to_dict()
# create an instance of AlgorithmAlgorithmData from a dict
algorithm_algorithm_data_from_dict = AlgorithmAlgorithmData.from_dict(algorithm_algorithm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


