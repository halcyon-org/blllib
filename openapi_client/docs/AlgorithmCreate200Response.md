# AlgorithmCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_id** | **str** | From Admin API | 
**algorithm_name** | **str** |  | 
**algorithm_description** | **str** |  | 
**need_external** | [**List[ExtInfoExtInfoId]**](ExtInfoExtInfoId.md) |  | 
**algorithm_scales** | **List[float]** |  | 
**algorithm_data_ids** | **List[str]** |  | 
**first_entry_at** | **datetime** |  | 
**last_entry_at** | **datetime** |  | 
**last_updated_at** | **datetime** |  | 
**api_key** | **str** |  | 

## Example

```python
from openapi_client.models.algorithm_create200_response import AlgorithmCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmCreate200Response from a JSON string
algorithm_create200_response_instance = AlgorithmCreate200Response.from_json(json)
# print the JSON string representation of the object
print(AlgorithmCreate200Response.to_json())

# convert the object into a dict
algorithm_create200_response_dict = algorithm_create200_response_instance.to_dict()
# create an instance of AlgorithmCreate200Response from a dict
algorithm_create200_response_from_dict = AlgorithmCreate200Response.from_dict(algorithm_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


