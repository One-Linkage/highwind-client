# highwind_client.HighwindResourcesApi

All URIs are relative to *https://api.ol.highwind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_verify_get_results_object_get**](HighwindResourcesApi.md#v3_verify_get_results_object_get) | **GET** /v3/verify/get_results/{object} | Return the result of the analysed PDF. Requires the &#x60;task_id&#x60; from &#x60;get_upload_url&#x60;.
[**v3_verify_get_results_object_options**](HighwindResourcesApi.md#v3_verify_get_results_object_options) | **OPTIONS** /v3/verify/get_results/{object} | 
[**v3_verify_get_upload_url_object_get**](HighwindResourcesApi.md#v3_verify_get_upload_url_object_get) | **GET** /v3/verify/get_upload_url/{object} | Generates a presigned URL for uploading to the storage system.
[**v3_verify_get_upload_url_object_options**](HighwindResourcesApi.md#v3_verify_get_upload_url_object_options) | **OPTIONS** /v3/verify/get_upload_url/{object} | 


# **v3_verify_get_results_object_get**
> V3VerifyGetResultsObjectGet200Response v3_verify_get_results_object_get(object)

Return the result of the analysed PDF. Requires the `task_id` from `get_upload_url`.

### Example

* Api Key Authentication (api_key):

```python
import highwind_client
from highwind_client.models.v3_verify_get_results_object_get200_response import V3VerifyGetResultsObjectGet200Response
from highwind_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ol.highwind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = highwind_client.Configuration(
    host = "https://api.ol.highwind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with highwind_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = highwind_client.HighwindResourcesApi(api_client)
    object = 'object_example' # str | Enter `task_id` value to retrieve associated summary.

    try:
        # Return the result of the analysed PDF. Requires the `task_id` from `get_upload_url`.
        api_response = api_instance.v3_verify_get_results_object_get(object)
        print("The response of HighwindResourcesApi->v3_verify_get_results_object_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HighwindResourcesApi->v3_verify_get_results_object_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Enter &#x60;task_id&#x60; value to retrieve associated summary. | 

### Return type

[**V3VerifyGetResultsObjectGet200Response**](V3VerifyGetResultsObjectGet200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_verify_get_results_object_options**
> DocTypes v3_verify_get_results_object_options(object)



### Example


```python
import highwind_client
from highwind_client.models.doc_types import DocTypes
from highwind_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ol.highwind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = highwind_client.Configuration(
    host = "https://api.ol.highwind.ai"
)


# Enter a context with an instance of the API client
with highwind_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = highwind_client.HighwindResourcesApi(api_client)
    object = 'object_example' # str | 

    try:
        api_response = api_instance.v3_verify_get_results_object_options(object)
        print("The response of HighwindResourcesApi->v3_verify_get_results_object_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HighwindResourcesApi->v3_verify_get_results_object_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**|  | 

### Return type

[**DocTypes**](DocTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_verify_get_upload_url_object_get**
> v3_verify_get_upload_url_object_get(document_type, object)

Generates a presigned URL for uploading to the storage system.

### Example

* Api Key Authentication (api_key):

```python
import highwind_client
from highwind_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ol.highwind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = highwind_client.Configuration(
    host = "https://api.ol.highwind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with highwind_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = highwind_client.HighwindResourcesApi(api_client)
    document_type = 'document_type_example' # str | Enter the appropriate document type for analysis. Options are: #magic___^_^___line - \"3mbs\" - 3 months bank statement - \"3mmar\" - 3 months management account report - \"afs\" - annual financial statement - \"bcl\" - bank certified letter - \"beea\" - black economic empowerment affidavit  - \"beec\" - black economic empowerment certificate  - \"cipc\" - companies and intellectual property commission - \"con\" - contract - \"cop\" - company profile - \"emp201\" - monthly employer declaration - \"i\" - invoice - \"id\" - certified identity - \"lgs\" - letter of good standing (coida) - \"po\" - purchase order - \"poa\" - proof of address - \"rl\" - reference letter - \"sc\" - shareholders certificate - \"tcc\" - tax clearance certificate #magic___^_^___line 
    object = 'object_example' # str | This value determines what the name of the file will be when uploaded to the system.

    try:
        # Generates a presigned URL for uploading to the storage system.
        api_instance.v3_verify_get_upload_url_object_get(document_type, object)
    except Exception as e:
        print("Exception when calling HighwindResourcesApi->v3_verify_get_upload_url_object_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**| Enter the appropriate document type for analysis. Options are: #magic___^_^___line - \&quot;3mbs\&quot; - 3 months bank statement - \&quot;3mmar\&quot; - 3 months management account report - \&quot;afs\&quot; - annual financial statement - \&quot;bcl\&quot; - bank certified letter - \&quot;beea\&quot; - black economic empowerment affidavit  - \&quot;beec\&quot; - black economic empowerment certificate  - \&quot;cipc\&quot; - companies and intellectual property commission - \&quot;con\&quot; - contract - \&quot;cop\&quot; - company profile - \&quot;emp201\&quot; - monthly employer declaration - \&quot;i\&quot; - invoice - \&quot;id\&quot; - certified identity - \&quot;lgs\&quot; - letter of good standing (coida) - \&quot;po\&quot; - purchase order - \&quot;poa\&quot; - proof of address - \&quot;rl\&quot; - reference letter - \&quot;sc\&quot; - shareholders certificate - \&quot;tcc\&quot; - tax clearance certificate #magic___^_^___line  | 
 **object** | **str**| This value determines what the name of the file will be when uploaded to the system. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_verify_get_upload_url_object_options**
> DocTypes v3_verify_get_upload_url_object_options(object)



### Example


```python
import highwind_client
from highwind_client.models.doc_types import DocTypes
from highwind_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ol.highwind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = highwind_client.Configuration(
    host = "https://api.ol.highwind.ai"
)


# Enter a context with an instance of the API client
with highwind_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = highwind_client.HighwindResourcesApi(api_client)
    object = 'object_example' # str | 

    try:
        api_response = api_instance.v3_verify_get_upload_url_object_options(object)
        print("The response of HighwindResourcesApi->v3_verify_get_upload_url_object_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HighwindResourcesApi->v3_verify_get_upload_url_object_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**|  | 

### Return type

[**DocTypes**](DocTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

