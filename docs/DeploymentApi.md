# swagger_client.DeploymentApi

All URIs are relative to */RadonCTT*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](DeploymentApi.md#create_deployment) | **POST** /deployment | Creates a deployment
[**delete_deployment_by_uuid**](DeploymentApi.md#delete_deployment_by_uuid) | **DELETE** /deployment/{deployment_uuid} | Delete a deployment
[**get_deployment_by_uuid**](DeploymentApi.md#get_deployment_by_uuid) | **GET** /deployment/{deployment_uuid} | Retrieve a deployment
[**get_deployments**](DeploymentApi.md#get_deployments) | **GET** /deployment | Get all deployments

# **create_deployment**
> create_deployment(body=body)

Creates a deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
body = swagger_client.POSTDeployment() # POSTDeployment |  (optional)

try:
    # Creates a deployment
    api_instance.create_deployment(body=body)
except ApiException as e:
    print("Exception when calling DeploymentApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTDeployment**](POSTDeployment.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment_by_uuid**
> Deployment delete_deployment_by_uuid(deployment_uuid)

Delete a deployment

Deletes the test artifact with the given UUID and all elements depending on it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
deployment_uuid = 'deployment_uuid_example' # str | UUID of the deployment to delete

try:
    # Delete a deployment
    api_response = api_instance.delete_deployment_by_uuid(deployment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->delete_deployment_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**| UUID of the deployment to delete | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_by_uuid**
> Deployment get_deployment_by_uuid(deployment_uuid)

Retrieve a deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
deployment_uuid = 'deployment_uuid_example' # str | UUID of the deployment to return

try:
    # Retrieve a deployment
    api_response = api_instance.get_deployment_by_uuid(deployment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployment_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**| UUID of the deployment to return | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> list[Deployment] get_deployments()

Get all deployments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()

try:
    # Get all deployments
    api_response = api_instance.get_deployments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Deployment]**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

