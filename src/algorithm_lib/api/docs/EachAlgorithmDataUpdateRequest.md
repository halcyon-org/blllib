# EachAlgorithmDataUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_data** | [**AlgorithmAlgorithmDataCreateOrUpdate**](AlgorithmAlgorithmDataCreateOrUpdate.md) |  | 

## Example

```python
from algorithm_lib.models.each_algorithm_data_update_request import EachAlgorithmDataUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EachAlgorithmDataUpdateRequest from a JSON string
each_algorithm_data_update_request_instance = EachAlgorithmDataUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EachAlgorithmDataUpdateRequest.to_json())

# convert the object into a dict
each_algorithm_data_update_request_dict = each_algorithm_data_update_request_instance.to_dict()
# create an instance of EachAlgorithmDataUpdateRequest from a dict
each_algorithm_data_update_request_from_dict = EachAlgorithmDataUpdateRequest.from_dict(each_algorithm_data_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


