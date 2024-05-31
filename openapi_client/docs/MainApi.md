# openapi_client.MainApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_create**](MainApi.md#algorithm_create) | **POST** /admin/algorithm | 
[**algorithm_delete**](MainApi.md#algorithm_delete) | **DELETE** /admin/algorithm/{algorithm_id} | 
[**algorithm_list**](MainApi.md#algorithm_list) | **GET** /algorithm | 
[**client_create**](MainApi.md#client_create) | **POST** /admin/client | 
[**client_delete**](MainApi.md#client_delete) | **POST** /admin/client/{client_id} | 
[**clients_get_client**](MainApi.md#clients_get_client) | **GET** /provider/clients | 
[**data_list**](MainApi.md#data_list) | **GET** /provider/data | 
[**each_algorithm_data_get**](MainApi.md#each_algorithm_data_get) | **GET** /algorithm/{algorithm_id}/data | 
[**each_algorithm_data_update**](MainApi.md#each_algorithm_data_update) | **PUT** /algorithm/{algorithm_id}/data | 
[**each_algorithm_get**](MainApi.md#each_algorithm_get) | **GET** /algorithm/{algorithm_id} | 
[**each_algorithm_update**](MainApi.md#each_algorithm_update) | **PUT** /algorithm/{algorithm_id} | 
[**each_data_get**](MainApi.md#each_data_get) | **GET** /provider/data/{altorithm_id} | 
[**each_ext_info_get**](MainApi.md#each_ext_info_get) | **GET** /extinfo/{extinfo_id} | 
[**ext_info_create**](MainApi.md#ext_info_create) | **POST** /admin/extinfo | 
[**ext_info_delete**](MainApi.md#ext_info_delete) | **DELETE** /admin/extinfo/{extinfo_id} | 
[**ext_info_list**](MainApi.md#ext_info_list) | **GET** /extinfo | 
[**hoge_get**](MainApi.md#hoge_get) | **GET** /extinfo/HOGE_ID/data | 
[**status_get**](MainApi.md#status_get) | **GET** /status | 


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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_create_request = openapi_client.AlgorithmCreateRequest() # AlgorithmCreateRequest | 

    try:
        api_response = api_instance.algorithm_create(algorithm_create_request)
        print("The response of MainApi->algorithm_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->algorithm_create: %s\n" % e)
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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 

    try:
        api_response = api_instance.algorithm_delete(algorithm_id)
        print("The response of MainApi->algorithm_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->algorithm_delete: %s\n" % e)
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

# **algorithm_list**
> List[AlgorithmAlgorithmInfomation] algorithm_list(limit=limit)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
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
    api_instance = openapi_client.MainApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.algorithm_list(limit=limit)
        print("The response of MainApi->algorithm_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->algorithm_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**List[AlgorithmAlgorithmInfomation]**](AlgorithmAlgorithmInfomation.md)

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
    api_instance = openapi_client.MainApi(api_client)
    client_create_request = openapi_client.ClientCreateRequest() # ClientCreateRequest | 

    try:
        api_response = api_instance.client_create(client_create_request)
        print("The response of MainApi->client_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->client_create: %s\n" % e)
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
    api_instance = openapi_client.MainApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        api_response = api_instance.client_delete(client_id)
        print("The response of MainApi->client_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->client_delete: %s\n" % e)
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

# **clients_get_client**
> ProviderClientData clients_get_client()



Get client of api key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
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
    api_instance = openapi_client.MainApi(api_client)

    try:
        api_response = api_instance.clients_get_client()
        print("The response of MainApi->clients_get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->clients_get_client: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProviderClientData**](ProviderClientData.md)

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

# **data_list**
> List[AlgorithmAlgorithmInfomation] data_list(limit=limit)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
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
    api_instance = openapi_client.MainApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.data_list(limit=limit)
        print("The response of MainApi->data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->data_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**List[AlgorithmAlgorithmInfomation]**](AlgorithmAlgorithmInfomation.md)

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

# **each_algorithm_data_get**
> AlgorithmAlgorithmData each_algorithm_data_get(algorithm_id, scale)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_data import AlgorithmAlgorithmData
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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    scale = 3.4 # float | 

    try:
        api_response = api_instance.each_algorithm_data_get(algorithm_id, scale)
        print("The response of MainApi->each_algorithm_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_algorithm_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_id** | **str**|  | 
 **scale** | **float**|  | 

### Return type

[**AlgorithmAlgorithmData**](AlgorithmAlgorithmData.md)

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

# **each_algorithm_data_update**
> AlgorithmAlgorithmData each_algorithm_data_update(algorithm_id, scale, each_algorithm_data_update_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_data import AlgorithmAlgorithmData
from openapi_client.models.each_algorithm_data_update_request import EachAlgorithmDataUpdateRequest
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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    scale = 3.4 # float | 
    each_algorithm_data_update_request = openapi_client.EachAlgorithmDataUpdateRequest() # EachAlgorithmDataUpdateRequest | 

    try:
        api_response = api_instance.each_algorithm_data_update(algorithm_id, scale, each_algorithm_data_update_request)
        print("The response of MainApi->each_algorithm_data_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_algorithm_data_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_id** | **str**|  | 
 **scale** | **float**|  | 
 **each_algorithm_data_update_request** | [**EachAlgorithmDataUpdateRequest**](EachAlgorithmDataUpdateRequest.md)|  | 

### Return type

[**AlgorithmAlgorithmData**](AlgorithmAlgorithmData.md)

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

# **each_algorithm_get**
> AlgorithmAlgorithmInfomation each_algorithm_get(algorithm_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 

    try:
        api_response = api_instance.each_algorithm_get(algorithm_id)
        print("The response of MainApi->each_algorithm_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_algorithm_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_id** | **str**|  | 

### Return type

[**AlgorithmAlgorithmInfomation**](AlgorithmAlgorithmInfomation.md)

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

# **each_algorithm_update**
> AlgorithmAlgorithmInfomation each_algorithm_update(algorithm_id, each_algorithm_update_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
from openapi_client.models.each_algorithm_update_request import EachAlgorithmUpdateRequest
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
    api_instance = openapi_client.MainApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    each_algorithm_update_request = openapi_client.EachAlgorithmUpdateRequest() # EachAlgorithmUpdateRequest | 

    try:
        api_response = api_instance.each_algorithm_update(algorithm_id, each_algorithm_update_request)
        print("The response of MainApi->each_algorithm_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_algorithm_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_id** | **str**|  | 
 **each_algorithm_update_request** | [**EachAlgorithmUpdateRequest**](EachAlgorithmUpdateRequest.md)|  | 

### Return type

[**AlgorithmAlgorithmInfomation**](AlgorithmAlgorithmInfomation.md)

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

# **each_data_get**
> AlgorithmAlgorithmData each_data_get(altorithm_id, type, algorithm_data_id=algorithm_data_id, area=area, until=until, until_entry=until_entry, scale=scale)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.algorithm_algorithm_data import AlgorithmAlgorithmData
from openapi_client.models.provider_request_type import ProviderRequestType
from openapi_client.models.types_date_date_until import TypesDateDateUntil
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
    api_instance = openapi_client.MainApi(api_client)
    altorithm_id = 'altorithm_id_example' # str | 
    type = openapi_client.ProviderRequestType() # ProviderRequestType | 
    algorithm_data_id = 'algorithm_data_id_example' # str |  (optional)
    area = openapi_client.TypesGeoJSONMultiPolygon() # TypesGeoJSONMultiPolygon |  (optional)
    until = openapi_client.TypesDateDateUntil() # TypesDateDateUntil |  (optional)
    until_entry = openapi_client.TypesDateDateUntil() # TypesDateDateUntil |  (optional)
    scale = 3.4 # float |  (optional)

    try:
        api_response = api_instance.each_data_get(altorithm_id, type, algorithm_data_id=algorithm_data_id, area=area, until=until, until_entry=until_entry, scale=scale)
        print("The response of MainApi->each_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **altorithm_id** | **str**|  | 
 **type** | [**ProviderRequestType**](.md)|  | 
 **algorithm_data_id** | **str**|  | [optional] 
 **area** | [**TypesGeoJSONMultiPolygon**](.md)|  | [optional] 
 **until** | [**TypesDateDateUntil**](.md)|  | [optional] 
 **until_entry** | [**TypesDateDateUntil**](.md)|  | [optional] 
 **scale** | **float**|  | [optional] 

### Return type

[**AlgorithmAlgorithmData**](AlgorithmAlgorithmData.md)

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

# **each_ext_info_get**
> ExtInfoExternalInfomation each_ext_info_get(extinfo_id)



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
    api_instance = openapi_client.MainApi(api_client)
    extinfo_id = openapi_client.ExtInfoExtInfoId() # ExtInfoExtInfoId | 

    try:
        api_response = api_instance.each_ext_info_get(extinfo_id)
        print("The response of MainApi->each_ext_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->each_ext_info_get: %s\n" % e)
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

# **ext_info_create**
> ExtInfoCreate200Response ext_info_create(ext_info_create_request)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_create200_response import ExtInfoCreate200Response
from openapi_client.models.ext_info_create_request import ExtInfoCreateRequest
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
    api_instance = openapi_client.MainApi(api_client)
    ext_info_create_request = openapi_client.ExtInfoCreateRequest() # ExtInfoCreateRequest | 

    try:
        api_response = api_instance.ext_info_create(ext_info_create_request)
        print("The response of MainApi->ext_info_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->ext_info_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_info_create_request** | [**ExtInfoCreateRequest**](ExtInfoCreateRequest.md)|  | 

### Return type

[**ExtInfoCreate200Response**](ExtInfoCreate200Response.md)

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
    api_instance = openapi_client.MainApi(api_client)
    extinfo_id = openapi_client.ExtInfoExtInfoId() # ExtInfoExtInfoId | 

    try:
        api_response = api_instance.ext_info_delete(extinfo_id)
        print("The response of MainApi->ext_info_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->ext_info_delete: %s\n" % e)
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
    api_instance = openapi_client.MainApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.ext_info_list(limit=limit)
        print("The response of MainApi->ext_info_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->ext_info_list: %s\n" % e)
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

# **hoge_get**
> List[HogeGet200ResponseInner] hoge_get(area=area)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.hoge_get200_response_inner import HogeGet200ResponseInner
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
    api_instance = openapi_client.MainApi(api_client)
    area = openapi_client.TypesGeoJSONMultiPolygon() # TypesGeoJSONMultiPolygon |  (optional)

    try:
        api_response = api_instance.hoge_get(area=area)
        print("The response of MainApi->hoge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->hoge_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | [**TypesGeoJSONMultiPolygon**](.md)|  | [optional] 

### Return type

[**List[HogeGet200ResponseInner]**](HogeGet200ResponseInner.md)

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

# **status_get**
> StatusData status_get()



### Example


```python
import openapi_client
from openapi_client.models.status_data import StatusData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MainApi(api_client)

    try:
        api_response = api_instance.status_get()
        print("The response of MainApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MainApi->status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusData**](StatusData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

