# openapi_client.KoyoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**each_koyo_data_new**](KoyoApi.md#each_koyo_data_new) | **PUT** /koyo/{koyo_id}/data | Put new data of own koyo
[**each_koyo_get**](KoyoApi.md#each_koyo_get) | **GET** /koyo/{koyo_id} | Get koyos&#39; basic information
[**each_koyo_update**](KoyoApi.md#each_koyo_update) | **PUT** /koyo/{koyo_id} | Update information on own koyo
[**koyo_list**](KoyoApi.md#koyo_list) | **GET** /koyo | Get a list of koyos&#39; basic information


# **each_koyo_data_new**
> KoyoKoyoData each_koyo_data_new(koyo_id, each_koyo_data_new_request)

Put new data of own koyo

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.each_koyo_data_new_request import EachKoyoDataNewRequest
from openapi_client.models.koyo_koyo_data import KoyoKoyoData
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
    api_instance = openapi_client.KoyoApi(api_client)
    koyo_id = 'koyo_id_example' # str | 
    each_koyo_data_new_request = openapi_client.EachKoyoDataNewRequest() # EachKoyoDataNewRequest | 

    try:
        # Put new data of own koyo
        api_response = api_instance.each_koyo_data_new(koyo_id, each_koyo_data_new_request)
        print("The response of KoyoApi->each_koyo_data_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KoyoApi->each_koyo_data_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_id** | **str**|  | 
 **each_koyo_data_new_request** | [**EachKoyoDataNewRequest**](EachKoyoDataNewRequest.md)|  | 

### Return type

[**KoyoKoyoData**](KoyoKoyoData.md)

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

# **each_koyo_get**
> KoyoKoyoInfomation each_koyo_get(koyo_id)

Get koyos' basic information

### Example


```python
import openapi_client
from openapi_client.models.koyo_koyo_infomation import KoyoKoyoInfomation
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
    api_instance = openapi_client.KoyoApi(api_client)
    koyo_id = 'koyo_id_example' # str | 

    try:
        # Get koyos' basic information
        api_response = api_instance.each_koyo_get(koyo_id)
        print("The response of KoyoApi->each_koyo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KoyoApi->each_koyo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_id** | **str**|  | 

### Return type

[**KoyoKoyoInfomation**](KoyoKoyoInfomation.md)

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

# **each_koyo_update**
> KoyoKoyoInfomation each_koyo_update(koyo_id, each_koyo_update_request)

Update information on own koyo

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.each_koyo_update_request import EachKoyoUpdateRequest
from openapi_client.models.koyo_koyo_infomation import KoyoKoyoInfomation
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
    api_instance = openapi_client.KoyoApi(api_client)
    koyo_id = 'koyo_id_example' # str | 
    each_koyo_update_request = openapi_client.EachKoyoUpdateRequest() # EachKoyoUpdateRequest | 

    try:
        # Update information on own koyo
        api_response = api_instance.each_koyo_update(koyo_id, each_koyo_update_request)
        print("The response of KoyoApi->each_koyo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KoyoApi->each_koyo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_id** | **str**|  | 
 **each_koyo_update_request** | [**EachKoyoUpdateRequest**](EachKoyoUpdateRequest.md)|  | 

### Return type

[**KoyoKoyoInfomation**](KoyoKoyoInfomation.md)

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

# **koyo_list**
> List[KoyoKoyoInfomation] koyo_list(limit=limit)

Get a list of koyos' basic information

### Example


```python
import openapi_client
from openapi_client.models.koyo_koyo_infomation import KoyoKoyoInfomation
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
    api_instance = openapi_client.KoyoApi(api_client)
    limit = 56 # int |  (optional)

    try:
        # Get a list of koyos' basic information
        api_response = api_instance.koyo_list(limit=limit)
        print("The response of KoyoApi->koyo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KoyoApi->koyo_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**List[KoyoKoyoInfomation]**](KoyoKoyoInfomation.md)

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

