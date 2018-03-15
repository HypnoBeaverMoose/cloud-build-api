# swagger_client.UserdevicesApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](UserdevicesApi.md#create_device) | **POST** /users/me/devices | Create iOS device profile
[**list_devices_for_user**](UserdevicesApi.md#list_devices_for_user) | **GET** /users/me/devices | List iOS device profiles


# **create_device**
> Options1 create_device(options)

Create iOS device profile

Create iOS device profile for the current user

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UserdevicesApi()
options = swagger_client.Options1() # Options1 | 

try: 
    # Create iOS device profile
    api_response = api_instance.create_device(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**Options1**](Options1.md)|  | 

### Return type

[**Options1**](Options1.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices_for_user**
> list[InlineResponse2005] list_devices_for_user()

List iOS device profiles

List all iOS device profiles for the current user

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UserdevicesApi()

try: 
    # List iOS device profiles
    api_response = api_instance.list_devices_for_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdevicesApi->list_devices_for_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

