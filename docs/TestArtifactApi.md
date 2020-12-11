# swagger_client.TestArtifactApi

All URIs are relative to */RadonCTT*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_testartifact**](TestArtifactApi.md#create_testartifact) | **POST** /testartifact | Creates a test artifact
[**delete_testartifact_by_uuid**](TestArtifactApi.md#delete_testartifact_by_uuid) | **DELETE** /testartifact/{testartifact_uuid} | Delete a test artifact
[**download_testartifact_by_uuid**](TestArtifactApi.md#download_testartifact_by_uuid) | **GET** /testartifact/{testartifact_uuid}/download | Downloads the generated test artifact
[**get_testartifact_by_uuid**](TestArtifactApi.md#get_testartifact_by_uuid) | **GET** /testartifact/{testartifact_uuid} | Retrieve a test artifact
[**get_testartifacts**](TestArtifactApi.md#get_testartifacts) | **GET** /testartifact | Get all test artifacts

# **create_testartifact**
> create_testartifact(body=body)

Creates a test artifact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestArtifactApi()
body = swagger_client.POSTTestArtifact() # POSTTestArtifact |  (optional)

try:
    # Creates a test artifact
    api_instance.create_testartifact(body=body)
except ApiException as e:
    print("Exception when calling TestArtifactApi->create_testartifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTTestArtifact**](POSTTestArtifact.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_testartifact_by_uuid**
> TestArtifact delete_testartifact_by_uuid(testartifact_uuid)

Delete a test artifact

Deletes the test artifact with the given UUID and all elements depending on it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestArtifactApi()
testartifact_uuid = 'testartifact_uuid_example' # str | UUID of the test artifact to delete

try:
    # Delete a test artifact
    api_response = api_instance.delete_testartifact_by_uuid(testartifact_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestArtifactApi->delete_testartifact_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testartifact_uuid** | **str**| UUID of the test artifact to delete | 

### Return type

[**TestArtifact**](TestArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_testartifact_by_uuid**
> str download_testartifact_by_uuid(testartifact_uuid)

Downloads the generated test artifact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestArtifactApi()
testartifact_uuid = 'testartifact_uuid_example' # str | UUID of the test artifact to download

try:
    # Downloads the generated test artifact
    api_response = api_instance.download_testartifact_by_uuid(testartifact_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestArtifactApi->download_testartifact_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testartifact_uuid** | **str**| UUID of the test artifact to download | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testartifact_by_uuid**
> TestArtifact get_testartifact_by_uuid(testartifact_uuid)

Retrieve a test artifact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestArtifactApi()
testartifact_uuid = 'testartifact_uuid_example' # str | UUID of the test artifact to return

try:
    # Retrieve a test artifact
    api_response = api_instance.get_testartifact_by_uuid(testartifact_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestArtifactApi->get_testartifact_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testartifact_uuid** | **str**| UUID of the test artifact to return | 

### Return type

[**TestArtifact**](TestArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testartifacts**
> list[TestArtifact] get_testartifacts()

Get all test artifacts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestArtifactApi()

try:
    # Get all test artifacts
    api_response = api_instance.get_testartifacts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestArtifactApi->get_testartifacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TestArtifact]**](TestArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

