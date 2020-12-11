# swagger_client.ProjectApi

All URIs are relative to */RadonCTT*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /project | Creates a project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /project/{project_uuid} | Delete a project
[**get_project_by_uuid**](ProjectApi.md#get_project_by_uuid) | **GET** /project/{project_uuid} | Retrieve a project
[**get_projects**](ProjectApi.md#get_projects) | **GET** /project | Get a list of all projects

# **create_project**
> create_project(body=body)

Creates a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.POSTProject() # POSTProject |  (optional)

try:
    # Creates a project
    api_instance.create_project(body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTProject**](POSTProject.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_uuid)

Delete a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_uuid = 'project_uuid_example' # str | UUID of the project to delete

try:
    # Delete a project
    api_instance.delete_project(project_uuid)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the project to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_uuid**
> Project get_project_by_uuid(project_uuid)

Retrieve a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
project_uuid = 'project_uuid_example' # str | UUID of the project to return

try:
    # Retrieve a project
    api_response = api_instance.get_project_by_uuid(project_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**| UUID of the project to return | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[Project] get_projects()

Get a list of all projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()

try:
    # Get a list of all projects
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

