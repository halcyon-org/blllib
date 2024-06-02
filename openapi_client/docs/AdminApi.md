# openapi_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_create**](AdminApi.md#algorithm_create) | **POST** /admin/algorithm | 
[**algorithm_delete**](AdminApi.md#algorithm_delete) | **DELETE** /admin/algorithm/{algorithm_id} | 
[**client_create**](AdminApi.md#client_create) | **POST** /admin/client | 
[**client_delete**](AdminApi.md#client_delete) | **POST** /admin/client/{client_id} | 
[**ext_info_create**](AdminApi.md#ext_info_create) | **POST** /admin/extinfo | 
[**ext_info_delete**](AdminApi.md#ext_info_delete) | **DELETE** /admin/extinfo/{extinfo_id} | 


# **algorithm_create**
> AlgorithmCreate200Response algorithm_create(algorithm_create_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_create200_response import AlgorithmCreate200Response
from openapi_client.models.algorithm_create_request import AlgorithmCreateRequest
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
    api_instance = openapi_client.AdminApi(api_client)
    algorithm_create_request = openapi_client.AlgorithmCreateRequest() # AlgorithmCreateRequest | 

    try:
        api_response = api_instance.algorithm_create(algorithm_create_request)
        print("The response of AdminApi->algorithm_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->algorithm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_create_request** | [**AlgorithmCreateRequest**](AlgorithmCreateRequest.md)|  | 

### Return type

[**AlgorithmCreate200Response**](AlgorithmCreate200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **algorithm_delete**
> AlgorithmDelete200Response algorithm_delete(algorithm_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_delete200_response import AlgorithmDelete200Response
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
    api_instance = openapi_client.AdminApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 

    try:
        api_response = api_instance.algorithm_delete(algorithm_id)
        print("The response of AdminApi->algorithm_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->algorithm_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_id** | **str**|  | 

### Return type

[**AlgorithmDelete200Response**](AlgorithmDelete200Response.md)

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

# **client_create**
> ProviderClientData client_create(client_create_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.client_create_request import ClientCreateRequest
from openapi_client.models.provider_client_data import ProviderClientData
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
    api_instance = openapi_client.AdminApi(api_client)
    client_create_request = openapi_client.ClientCreateRequest() # ClientCreateRequest | 

    try:
        api_response = api_instance.client_create(client_create_request)
        print("The response of AdminApi->client_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->client_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_create_request** | [**ClientCreateRequest**](ClientCreateRequest.md)|  | 

### Return type

[**ProviderClientData**](ProviderClientData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_delete**
> ClientDelete200Response client_delete(client_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.client_delete200_response import ClientDelete200Response
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
    api_instance = openapi_client.AdminApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        api_response = api_instance.client_delete(client_id)
        print("The response of AdminApi->client_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->client_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**ClientDelete200Response**](ClientDelete200Response.md)

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

# **ext_info_create**
> ExtInfoExternalInfomation ext_info_create(ext_info_create_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_create_request import ExtInfoCreateRequest
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
    api_instance = openapi_client.AdminApi(api_client)
    ext_info_create_request = openapi_client.ExtInfoCreateRequest() # ExtInfoCreateRequest | 

    try:
        api_response = api_instance.ext_info_create(ext_info_create_request)
        print("The response of AdminApi->ext_info_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->ext_info_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_info_create_request** | [**ExtInfoCreateRequest**](ExtInfoCreateRequest.md)|  | 

### Return type

[**ExtInfoExternalInfomation**](ExtInfoExternalInfomation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ext_info_delete**
> ExtInfoDelete200Response ext_info_delete(extinfo_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_delete200_response import ExtInfoDelete200Response
from openapi_client.models.ext_info_ext_info_id import ExtInfoExtInfoId
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
    api_instance = openapi_client.AdminApi(api_client)
    extinfo_id = openapi_client.ExtInfoExtInfoId() # ExtInfoExtInfoId | 

    try:
        api_response = api_instance.ext_info_delete(extinfo_id)
        print("The response of AdminApi->ext_info_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->ext_info_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extinfo_id** | [**ExtInfoExtInfoId**](.md)|  | 

### Return type

[**ExtInfoDelete200Response**](ExtInfoDelete200Response.md)

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

