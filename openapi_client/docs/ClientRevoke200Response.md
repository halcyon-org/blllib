# ClientRevoke200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**api_key** | **str** |  | 

## Example

```python
from openapi_client.models.client_revoke200_response import ClientRevoke200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRevoke200Response from a JSON string
client_revoke200_response_instance = ClientRevoke200Response.from_json(json)
# print the JSON string representation of the object
print(ClientRevoke200Response.to_json())

# convert the object into a dict
client_revoke200_response_dict = client_revoke200_response_instance.to_dict()
# create an instance of ClientRevoke200Response from a dict
client_revoke200_response_from_dict = ClientRevoke200Response.from_dict(client_revoke200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


