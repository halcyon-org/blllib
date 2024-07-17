# openapi_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_create**](AdminApi.md#client_create) | **POST** /admin/client | 
[**client_delete**](AdminApi.md#client_delete) | **POST** /admin/client/{client_id} | 
[**client_list**](AdminApi.md#client_list) | **GET** /admin/client | 
[**client_revoke**](AdminApi.md#client_revoke) | **PUT** /admin/client | 
[**ext_info_create**](AdminApi.md#ext_info_create) | **POST** /admin/extinfo | 
[**ext_info_delete**](AdminApi.md#ext_info_delete) | **DELETE** /admin/extinfo/{extinfo_id} | 
[**ext_info_revoke**](AdminApi.md#ext_info_revoke) | **PUT** /admin/extinfo/{extinfo_id} | 
[**koyo_create**](AdminApi.md#koyo_create) | **POST** /admin/koyo | Create new koyo information
[**koyo_delete**](AdminApi.md#koyo_delete) | **DELETE** /admin/koyo/{koyo_id} | Delete koyo information
[**koyo_revoke**](AdminApi.md#koyo_revoke) | **PUT** /admin/koyo/{koyo_id} | Revoke koyo api key


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

# **client_list**
> List[ProviderClientData] client_list(limit=limit)



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
    api_instance = openapi_client.AdminApi(api_client)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.client_list(limit=limit)
        print("The response of AdminApi->client_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->client_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**List[ProviderClientData]**](ProviderClientData.md)

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

# **client_revoke**
> ProviderClientData client_revoke(client_id)



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
    api_instance = openapi_client.AdminApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        api_response = api_instance.client_revoke(client_id)
        print("The response of AdminApi->client_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->client_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **ext_info_revoke**
> ExtInfoRevoke200Response ext_info_revoke(extinfo_id)



### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ext_info_ext_info_id import ExtInfoExtInfoId
from openapi_client.models.ext_info_revoke200_response import ExtInfoRevoke200Response
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
        api_response = api_instance.ext_info_revoke(extinfo_id)
        print("The response of AdminApi->ext_info_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->ext_info_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extinfo_id** | [**ExtInfoExtInfoId**](.md)|  | 

### Return type

[**ExtInfoRevoke200Response**](ExtInfoRevoke200Response.md)

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

# **koyo_create**
> KoyoCreate200Response koyo_create(koyo_create_request)

Create new koyo information

Set up koyo's basic information and register it in the database. You can get koyo_id by hitting this endpoint. For updating basic information, please use /koyo api instead of admin api

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.koyo_create200_response import KoyoCreate200Response
from openapi_client.models.koyo_create_request import KoyoCreateRequest
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
    koyo_create_request = openapi_client.KoyoCreateRequest() # KoyoCreateRequest | 

    try:
        # Create new koyo information
        api_response = api_instance.koyo_create(koyo_create_request)
        print("The response of AdminApi->koyo_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->koyo_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_create_request** | [**KoyoCreateRequest**](KoyoCreateRequest.md)|  | 

### Return type

[**KoyoCreate200Response**](KoyoCreate200Response.md)

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

# **koyo_delete**
> KoyoDelete200Response koyo_delete(koyo_id)

Delete koyo information

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.koyo_delete200_response import KoyoDelete200Response
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
    koyo_id = 'koyo_id_example' # str | 

    try:
        # Delete koyo information
        api_response = api_instance.koyo_delete(koyo_id)
        print("The response of AdminApi->koyo_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->koyo_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_id** | **str**|  | 

### Return type

[**KoyoDelete200Response**](KoyoDelete200Response.md)

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

# **koyo_revoke**
> KoyoRevoke200Response koyo_revoke(koyo_id)

Revoke koyo api key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.koyo_revoke200_response import KoyoRevoke200Response
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
    koyo_id = 'koyo_id_example' # str | 

    try:
        # Revoke koyo api key
        api_response = api_instance.koyo_revoke(koyo_id)
        print("The response of AdminApi->koyo_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->koyo_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **koyo_id** | **str**|  | 

### Return type

[**KoyoRevoke200Response**](KoyoRevoke200Response.md)

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

