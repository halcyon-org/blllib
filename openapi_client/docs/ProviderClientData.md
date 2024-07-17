# ProviderClientData

Data for the client to use the provider api.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**username** | **str** |  | 
**api_key** | **str** |  | 
**created_at** | **datetime** |  | 
**last_used_at** | **datetime** | The last time the client used the api. | 
**last_updated_at** | **datetime** | The last time the client updated the data. | 

## Example

```python
from openapi_client.models.provider_client_data import ProviderClientData

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderClientData from a JSON string
provider_client_data_instance = ProviderClientData.from_json(json)
# print the JSON string representation of the object
print(ProviderClientData.to_json())

# convert the object into a dict
provider_client_data_dict = provider_client_data_instance.to_dict()
# create an instance of ProviderClientData from a dict
provider_client_data_from_dict = ProviderClientData.from_dict(provider_client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


