# swagger_client.ConfigApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unity_versions**](ConfigApi.md#list_unity_versions) | **GET** /versions/unity | List all unity versions
[**list_xcode_versions**](ConfigApi.md#list_xcode_versions) | **GET** /versions/xcode | List all xcode versions


# **list_unity_versions**
> list[InlineResponse200] list_unity_versions()

List all unity versions

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
api_instance = swagger_client.ConfigApi()

try: 
    # List all unity versions
    api_response = api_instance.list_unity_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_unity_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_xcode_versions**
> list[InlineResponse2001] list_xcode_versions()

List all xcode versions

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
api_instance = swagger_client.ConfigApi()

try: 
    # List all xcode versions
    api_response = api_instance.list_xcode_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_xcode_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

