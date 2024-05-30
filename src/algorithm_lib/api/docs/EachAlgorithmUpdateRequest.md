# EachAlgorithmUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_algorithm** | [**AlgorithmAlgorithmInfomationCreateOrUpdate**](AlgorithmAlgorithmInfomationCreateOrUpdate.md) |  | 

## Example

```python
from algorithm_lib.models.each_algorithm_update_request import EachAlgorithmUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EachAlgorithmUpdateRequest from a JSON string
each_algorithm_update_request_instance = EachAlgorithmUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EachAlgorithmUpdateRequest.to_json())

# convert the object into a dict
each_algorithm_update_request_dict = each_algorithm_update_request_instance.to_dict()
# create an instance of EachAlgorithmUpdateRequest from a dict
each_algorithm_update_request_from_dict = EachAlgorithmUpdateRequest.from_dict(each_algorithm_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


