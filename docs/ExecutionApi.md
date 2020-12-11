# swagger_client.ExecutionApi

All URIs are relative to */RadonCTT*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution**](ExecutionApi.md#create_execution) | **POST** /execution | Creates an execution
[**delete_execution_by_uuid**](ExecutionApi.md#delete_execution_by_uuid) | **DELETE** /execution/{execution_uuid} | Delete an execution
[**get_execution_by_uuid**](ExecutionApi.md#get_execution_by_uuid) | **GET** /execution/{execution_uuid} | Retrieve an execution
[**get_executions**](ExecutionApi.md#get_executions) | **GET** /execution | Get all executions

# **create_execution**
> create_execution(body=body)

Creates an execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecutionApi()
body = swagger_client.POSTExecution() # POSTExecution |  (optional)

try:
    # Creates an execution
    api_instance.create_execution(body=body)
except ApiException as e:
    print("Exception when calling ExecutionApi->create_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTExecution**](POSTExecution.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_execution_by_uuid**
> Execution delete_execution_by_uuid(execution_uuid)

Delete an execution

Deletes the execution with the given UUID and all elements depending on it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecutionApi()
execution_uuid = 'execution_uuid_example' # str | UUID of the execution to delete

try:
    # Delete an execution
    api_response = api_instance.delete_execution_by_uuid(execution_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionApi->delete_execution_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_uuid** | **str**| UUID of the execution to delete | 

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_by_uuid**
> Execution get_execution_by_uuid(execution_uuid)

Retrieve an execution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecutionApi()
execution_uuid = 'execution_uuid_example' # str | UUID of the execution to return

try:
    # Retrieve an execution
    api_response = api_instance.get_execution_by_uuid(execution_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionApi->get_execution_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_uuid** | **str**| UUID of the execution to return | 

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executions**
> list[Execution] get_executions()

Get all executions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecutionApi()

try:
    # Get all executions
    api_response = api_instance.get_executions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecutionApi->get_executions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Execution]**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

