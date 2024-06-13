# AlgorithmAlgorithmInfomation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_id** | **str** | From Admin API | 
**algorithm_name** | **str** |  | 
**algorithm_description** | **str** |  | 
**need_external** | [**List[ExtInfoExtInfoId]**](ExtInfoExtInfoId.md) |  | 
**algorithm_params** | **Dict[str, str]** | param name: param default | 
**algorithm_scales** | **List[float]** |  | 
**algorithm_data_ids** | **List[str]** |  | 
**version** | **str** | Semantic versioning | 
**first_entry_at** | **datetime** |  | 
**last_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmAlgorithmInfomation from a JSON string
algorithm_algorithm_infomation_instance = AlgorithmAlgorithmInfomation.from_json(json)
# print the JSON string representation of the object
print(AlgorithmAlgorithmInfomation.to_json())

# convert the object into a dict
algorithm_algorithm_infomation_dict = algorithm_algorithm_infomation_instance.to_dict()
# create an instance of AlgorithmAlgorithmInfomation from a dict
algorithm_algorithm_infomation_from_dict = AlgorithmAlgorithmInfomation.from_dict(algorithm_algorithm_infomation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


