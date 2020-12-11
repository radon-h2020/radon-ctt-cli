# swagger_client.ResultApi

All URIs are relative to */RadonCTT*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_result**](ResultApi.md#create_result) | **POST** /result | Creates new result
[**delete_result_by_uuid**](ResultApi.md#delete_result_by_uuid) | **DELETE** /result/{result_uuid} | Delete a result
[**download_result_by_uuid**](ResultApi.md#download_result_by_uuid) | **GET** /result/{result_uuid}/download | Downloads the generated results
[**get_result_by_uuid**](ResultApi.md#get_result_by_uuid) | **GET** /result/{result_uuid} | Retrieve a result
[**get_results**](ResultApi.md#get_results) | **GET** /result | Get all results

# **create_result**
> create_result(body=body)

Creates new result

Creates a new result based on a previously run execution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
body = swagger_client.POSTResult() # POSTResult |  (optional)

try:
    # Creates new result
    api_instance.create_result(body=body)
except ApiException as e:
    print("Exception when calling ResultApi->create_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTResult**](POSTResult.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_result_by_uuid**
> Result delete_result_by_uuid(result_uuid)

Delete a result

Deletes the result with the given UUID on it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_uuid = 'result_uuid_example' # str | UUID of the result to delete

try:
    # Delete a result
    api_response = api_instance.delete_result_by_uuid(result_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->delete_result_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_uuid** | **str**| UUID of the result to delete | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_result_by_uuid**
> str download_result_by_uuid(result_uuid)

Downloads the generated results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_uuid = 'result_uuid_example' # str | UUID of the result to download

try:
    # Downloads the generated results
    api_response = api_instance.download_result_by_uuid(result_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->download_result_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_uuid** | **str**| UUID of the result to download | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_by_uuid**
> Result get_result_by_uuid(result_uuid)

Retrieve a result

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
result_uuid = 'result_uuid_example' # str | UUID of the result to return

try:
    # Retrieve a result
    api_response = api_instance.get_result_by_uuid(result_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_result_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_uuid** | **str**| UUID of the result to return | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_results**
> list[Result] get_results()

Get all results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()

try:
    # Get all results
    api_response = api_instance.get_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Result]**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

