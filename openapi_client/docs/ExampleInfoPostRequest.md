# ExampleInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExtInfoExampleInfoExampleData]**](ExtInfoExampleInfoExampleData.md) |  | 

## Example

```python
from openapi_client.models.example_info_post_request import ExampleInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleInfoPostRequest from a JSON string
example_info_post_request_instance = ExampleInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(ExampleInfoPostRequest.to_json())

# convert the object into a dict
example_info_post_request_dict = example_info_post_request_instance.to_dict()
# create an instance of ExampleInfoPostRequest from a dict
example_info_post_request_from_dict = ExampleInfoPostRequest.from_dict(example_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


