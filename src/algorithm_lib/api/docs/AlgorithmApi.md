# algorithm_lib.AlgorithmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**algorithm_list**](AlgorithmApi.md#algorithm_list) | **GET** /algorithm | 
[**each_algorithm_data_get**](AlgorithmApi.md#each_algorithm_data_get) | **GET** /algorithm/{algorithm_id}/data | 
[**each_algorithm_data_update**](AlgorithmApi.md#each_algorithm_data_update) | **PUT** /algorithm/{algorithm_id}/data | 
[**each_algorithm_get**](AlgorithmApi.md#each_algorithm_get) | **GET** /algorithm/{algorithm_id} | 
[**each_algorithm_update**](AlgorithmApi.md#each_algorithm_update) | **PUT** /algorithm/{algorithm_id} | 


# **algorithm_list**
> List[AlgorithmAlgorithmInfomation] algorithm_list(limit=limit)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import algorithm_lib
from algorithm_lib.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
from algorithm_lib.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = algorithm_lib.Configuration(
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
with algorithm_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = algorithm_lib.AlgorithmApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.algorithm_list(limit=limit)
        print("The response of AlgorithmApi->algorithm_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgorithmApi->algorithm_list: %s\n" % e)
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
import algorithm_lib
from algorithm_lib.models.algorithm_algorithm_data import AlgorithmAlgorithmData
from algorithm_lib.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = algorithm_lib.Configuration(
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
with algorithm_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = algorithm_lib.AlgorithmApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    scale = 3.4 # float | 

    try:
        api_response = api_instance.each_algorithm_data_get(algorithm_id, scale)
        print("The response of AlgorithmApi->each_algorithm_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgorithmApi->each_algorithm_data_get: %s\n" % e)
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
import algorithm_lib
from algorithm_lib.models.algorithm_algorithm_data import AlgorithmAlgorithmData
from algorithm_lib.models.each_algorithm_data_update_request import EachAlgorithmDataUpdateRequest
from algorithm_lib.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = algorithm_lib.Configuration(
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
with algorithm_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = algorithm_lib.AlgorithmApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    scale = 3.4 # float | 
    each_algorithm_data_update_request = algorithm_lib.EachAlgorithmDataUpdateRequest() # EachAlgorithmDataUpdateRequest | 

    try:
        api_response = api_instance.each_algorithm_data_update(algorithm_id, scale, each_algorithm_data_update_request)
        print("The response of AlgorithmApi->each_algorithm_data_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgorithmApi->each_algorithm_data_update: %s\n" % e)
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
import algorithm_lib
from algorithm_lib.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
from algorithm_lib.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = algorithm_lib.Configuration(
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
with algorithm_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = algorithm_lib.AlgorithmApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 

    try:
        api_response = api_instance.each_algorithm_get(algorithm_id)
        print("The response of AlgorithmApi->each_algorithm_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgorithmApi->each_algorithm_get: %s\n" % e)
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
import algorithm_lib
from algorithm_lib.models.algorithm_algorithm_infomation import AlgorithmAlgorithmInfomation
from algorithm_lib.models.each_algorithm_update_request import EachAlgorithmUpdateRequest
from algorithm_lib.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = algorithm_lib.Configuration(
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
with algorithm_lib.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = algorithm_lib.AlgorithmApi(api_client)
    algorithm_id = 'algorithm_id_example' # str | 
    each_algorithm_update_request = algorithm_lib.EachAlgorithmUpdateRequest() # EachAlgorithmUpdateRequest | 

    try:
        api_response = api_instance.each_algorithm_update(algorithm_id, each_algorithm_update_request)
        print("The response of AlgorithmApi->each_algorithm_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlgorithmApi->each_algorithm_update: %s\n" % e)
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

