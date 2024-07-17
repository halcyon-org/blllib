# ProviderClientDataCreate

Data for the client to use the provider api.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 

## Example

```python
from openapi_client.models.provider_client_data_create import ProviderClientDataCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderClientDataCreate from a JSON string
provider_client_data_create_instance = ProviderClientDataCreate.from_json(json)
# print the JSON string representation of the object
print(ProviderClientDataCreate.to_json())

# convert the object into a dict
provider_client_data_create_dict = provider_client_data_create_instance.to_dict()
# create an instance of ProviderClientDataCreate from a dict
provider_client_data_create_from_dict = ProviderClientDataCreate.from_dict(provider_client_data_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


