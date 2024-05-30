# AlgorithmAlgorithmInfomationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_name** | **str** |  | 
**algorithm_description** | **str** |  | 
**need_external** | [**List[ExtInfoExtInfoId]**](ExtInfoExtInfoId.md) |  | 
**algorithm_scales** | **List[float]** |  | 
**algorithm_data_ids** | **List[str]** |  | 

## Example

```python
from algorithm_lib.models.algorithm_algorithm_infomation_create import AlgorithmAlgorithmInfomationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmAlgorithmInfomationCreate from a JSON string
algorithm_algorithm_infomation_create_instance = AlgorithmAlgorithmInfomationCreate.from_json(json)
# print the JSON string representation of the object
print(AlgorithmAlgorithmInfomationCreate.to_json())

# convert the object into a dict
algorithm_algorithm_infomation_create_dict = algorithm_algorithm_infomation_create_instance.to_dict()
# create an instance of AlgorithmAlgorithmInfomationCreate from a dict
algorithm_algorithm_infomation_create_from_dict = AlgorithmAlgorithmInfomationCreate.from_dict(algorithm_algorithm_infomation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


