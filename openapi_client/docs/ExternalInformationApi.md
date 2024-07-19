# openapi_client.ExternalInformationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_info_get**](ExternalInformationApi.md#example_info_get) | **GET** /extinfo/example_id/data | Get example data endpoint
[**example_info_post**](ExternalInformationApi.md#example_info_post) | **POST** /extinfo/example_id/data | Post example data endpoint
[**ext_info_get**](ExternalInformationApi.md#ext_info_get) | **GET** /extinfo/{extinfo_id} | 
[**ext_info_list**](ExternalInformationApi.md#ext_info_list) | **GET** /extinfo | 


# **example_info_get**
> List[ExampleInfoGet200ResponseInner] example_info_get(area=area)

Get example data endpoint

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.example_info_get200_response_inner import ExampleInfoGet200ResponseInner
from openapi_client.models.types_geo_json_multi_polygon import TypesGeoJSONMultiPolygon
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExternalInformationApi(api_client)
    area = openapi_client.TypesGeoJSONMultiPolygon() # TypesGeoJSONMultiPolygon |  (optional)

    try:
        # Get example data endpoint
        api_response = api_instance.example_info_get(area=area)
        print("The response of ExternalInformationApi->example_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->example_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | [**TypesGeoJSONMultiPolygon**](.md)|  | [optional] 

### Return type

[**List[ExampleInfoGet200ResponseInner]**](ExampleInfoGet200ResponseInner.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **example_info_post**
> example_info_post(example_info_post_request)

Post example data endpoint

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.example_info_post_request import ExampleInfoPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExternalInformationApi(api_client)
    example_info_post_request = openapi_client.ExampleInfoPostRequest() # ExampleInfoPostRequest | 

    try:
        # Post example data endpoint
        api_instance.example_info_post(example_info_post_request)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->example_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **example_info_post_request** | [**ExampleInfoPostRequest**](ExampleInfoPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ext_info_get**
> ExtInfoExternalInfomation ext_info_get(extinfo_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_ext_info_id import ExtInfoExtInfoId
from openapi_client.models.ext_info_external_infomation import ExtInfoExternalInfomation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExternalInformationApi(api_client)
    extinfo_id = openapi_client.ExtInfoExtInfoId() # ExtInfoExtInfoId | 

    try:
        api_response = api_instance.ext_info_get(extinfo_id)
        print("The response of ExternalInformationApi->ext_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->ext_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extinfo_id** | [**ExtInfoExtInfoId**](.md)|  | 

### Return type

[**ExtInfoExternalInfomation**](ExtInfoExternalInfomation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ext_info_list**
> List[ExtInfoExternalInfomation] ext_info_list(limit=limit)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_external_infomation import ExtInfoExternalInfomation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExternalInformationApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.ext_info_list(limit=limit)
        print("The response of ExternalInformationApi->ext_info_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->ext_info_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**List[ExtInfoExternalInfomation]**](ExtInfoExternalInfomation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

