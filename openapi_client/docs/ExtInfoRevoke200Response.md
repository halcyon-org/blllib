# ExtInfoRevoke200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extinfo_id** | [**ExtInfoExtInfoId**](ExtInfoExtInfoId.md) |  | 
**api_key** | **str** |  | 

## Example

```python
from openapi_client.models.ext_info_revoke200_response import ExtInfoRevoke200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExtInfoRevoke200Response from a JSON string
ext_info_revoke200_response_instance = ExtInfoRevoke200Response.from_json(json)
# print the JSON string representation of the object
print(ExtInfoRevoke200Response.to_json())

# convert the object into a dict
ext_info_revoke200_response_dict = ext_info_revoke200_response_instance.to_dict()
# create an instance of ExtInfoRevoke200Response from a dict
ext_info_revoke200_response_from_dict = ExtInfoRevoke200Response.from_dict(ext_info_revoke200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


