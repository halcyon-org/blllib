# AlgorithmCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**AlgorithmAlgorithmInfomationCreate**](AlgorithmAlgorithmInfomationCreate.md) |  | 

## Example

```python
from openapi_client.models.algorithm_create_request import AlgorithmCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmCreateRequest from a JSON string
algorithm_create_request_instance = AlgorithmCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AlgorithmCreateRequest.to_json())

# convert the object into a dict
algorithm_create_request_dict = algorithm_create_request_instance.to_dict()
# create an instance of AlgorithmCreateRequest from a dict
algorithm_create_request_from_dict = AlgorithmCreateRequest.from_dict(algorithm_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


