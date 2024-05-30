# AlgorithmAlgorithmDataCreateOrUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_id** | **str** |  | 
**algorithm_scale** | **float** |  | 
**content_type** | [**AlgorithmDataType**](AlgorithmDataType.md) |  | 
**content** | **bytearray** |  | 

## Example

```python
from algorithm_lib.models.algorithm_algorithm_data_create_or_update import AlgorithmAlgorithmDataCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmAlgorithmDataCreateOrUpdate from a JSON string
algorithm_algorithm_data_create_or_update_instance = AlgorithmAlgorithmDataCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print(AlgorithmAlgorithmDataCreateOrUpdate.to_json())

# convert the object into a dict
algorithm_algorithm_data_create_or_update_dict = algorithm_algorithm_data_create_or_update_instance.to_dict()
# create an instance of AlgorithmAlgorithmDataCreateOrUpdate from a dict
algorithm_algorithm_data_create_or_update_from_dict = AlgorithmAlgorithmDataCreateOrUpdate.from_dict(algorithm_algorithm_data_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


