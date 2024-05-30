# openapi_client.ProviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_get_client**](ProviderApi.md#clients_get_client) | **GET** /provider/clients | 
[**data_list**](ProviderApi.md#data_list) | **GET** /provider/data | 
[**each_data_get**](ProviderApi.md#each_data_get) | **GET** /provider/data/{altorithm_id} | 


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
    api_instance = openapi_client.ProviderApi(api_client)

    try:
        api_response = api_instance.clients_get_client()
        print("The response of ProviderApi->clients_get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->clients_get_client: %s\n" % e)
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
    api_instance = openapi_client.ProviderApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.data_list(limit=limit)
        print("The response of ProviderApi->data_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->data_list: %s\n" % e)
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
    api_instance = openapi_client.ProviderApi(api_client)
    altorithm_id = 'altorithm_id_example' # str | 
    type = openapi_client.ProviderRequestType() # ProviderRequestType | 
    algorithm_data_id = 'algorithm_data_id_example' # str |  (optional)
    area = openapi_client.TypesGeoJSONMultiPolygon() # TypesGeoJSONMultiPolygon |  (optional)
    until = openapi_client.TypesDateDateUntil() # TypesDateDateUntil |  (optional)
    until_entry = openapi_client.TypesDateDateUntil() # TypesDateDateUntil |  (optional)
    scale = 3.4 # float |  (optional)

    try:
        api_response = api_instance.each_data_get(altorithm_id, type, algorithm_data_id=algorithm_data_id, area=area, until=until, until_entry=until_entry, scale=scale)
        print("The response of ProviderApi->each_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->each_data_get: %s\n" % e)
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

