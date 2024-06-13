# AlgorithmAlgorithmInfomationCreateOrUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_id** | **str** | From Admin API | 
**algorithm_name** | **str** |  | 
**algorithm_description** | **str** |  | 
**need_external** | [**List[ExtInfoExtInfoId]**](ExtInfoExtInfoId.md) |  | 
**algorithm_scales** | **List[float]** |  | 
**algorithm_data_ids** | **List[str]** |  | 
**version** | **str** | Semantic versioning | 

## Example

```python
from openapi_client.models.algorithm_algorithm_infomation_create_or_update import AlgorithmAlgorithmInfomationCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmAlgorithmInfomationCreateOrUpdate from a JSON string
algorithm_algorithm_infomation_create_or_update_instance = AlgorithmAlgorithmInfomationCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print(AlgorithmAlgorithmInfomationCreateOrUpdate.to_json())

# convert the object into a dict
algorithm_algorithm_infomation_create_or_update_dict = algorithm_algorithm_infomation_create_or_update_instance.to_dict()
# create an instance of AlgorithmAlgorithmInfomationCreateOrUpdate from a dict
algorithm_algorithm_infomation_create_or_update_from_dict = AlgorithmAlgorithmInfomationCreateOrUpdate.from_dict(algorithm_algorithm_infomation_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


