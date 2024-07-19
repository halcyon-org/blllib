# ExampleInfoGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**data** | [**ExtInfoExampleInfoExampleData**](ExtInfoExampleInfoExampleData.md) |  | 

## Example

```python
from openapi_client.models.example_info_get200_response_inner import ExampleInfoGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleInfoGet200ResponseInner from a JSON string
example_info_get200_response_inner_instance = ExampleInfoGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ExampleInfoGet200ResponseInner.to_json())

# convert the object into a dict
example_info_get200_response_inner_dict = example_info_get200_response_inner_instance.to_dict()
# create an instance of ExampleInfoGet200ResponseInner from a dict
example_info_get200_response_inner_from_dict = ExampleInfoGet200ResponseInner.from_dict(example_info_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


