# algorithm_lib.ExternalInformationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**each_ext_info_get**](ExternalInformationApi.md#each_ext_info_get) | **GET** /extinfo/{extinfo_id} | 
[**ext_info_list**](ExternalInformationApi.md#ext_info_list) | **GET** /extinfo | 
[**hoge_get**](ExternalInformationApi.md#hoge_get) | **GET** /extinfo/HOGE_ID/data | 


# **each_ext_info_get**
> ExtInfoExternalInfomation each_ext_info_get(extinfo_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import algorithm_lib
from algorithm_lib.models.ext_info_ext_info_id import ExtInfoExtInfoId
from algorithm_lib.models.ext_info_external_infomation import ExtInfoExternalInfomation
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
    api_instance = algorithm_lib.ExternalInformationApi(api_client)
    extinfo_id = algorithm_lib.ExtInfoExtInfoId() # ExtInfoExtInfoId | 

    try:
        api_response = api_instance.each_ext_info_get(extinfo_id)
        print("The response of ExternalInformationApi->each_ext_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->each_ext_info_get: %s\n" % e)
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
import algorithm_lib
from algorithm_lib.models.ext_info_external_infomation import ExtInfoExternalInfomation
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
    api_instance = algorithm_lib.ExternalInformationApi(api_client)
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

# **hoge_get**
> List[HogeGet200ResponseInner] hoge_get(area=area)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import algorithm_lib
from algorithm_lib.models.hoge_get200_response_inner import HogeGet200ResponseInner
from algorithm_lib.models.types_geo_json_multi_polygon import TypesGeoJSONMultiPolygon
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
    api_instance = algorithm_lib.ExternalInformationApi(api_client)
    area = algorithm_lib.TypesGeoJSONMultiPolygon() # TypesGeoJSONMultiPolygon |  (optional)

    try:
        api_response = api_instance.hoge_get(area=area)
        print("The response of ExternalInformationApi->hoge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalInformationApi->hoge_get: %s\n" % e)
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

