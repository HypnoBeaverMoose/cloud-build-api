# swagger_client.SharesApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_share_metadata**](SharesApi.md#get_share_metadata) | **GET** /shares/{shareid} | Get details on shared build including download link


# **get_share_metadata**
> OrgsorgidprojectsprojectidbuildtargetsBuilds get_share_metadata(shareid, include=include)

Get details on shared build including download link

This is an endpoint accessible without an api key that provides information about a specific build including download links. A shareid is generated by POSTing to a <a href=\"#!/builds/createShare\">build's share endpoint</a>.

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
api_instance = swagger_client.SharesApi()
shareid = 'shareid_example' # str | 
include = 'include_example' # str | Extra fields to include in the response (optional)

try: 
    # Get details on shared build including download link
    api_response = api_instance.get_share_metadata(shareid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->get_share_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shareid** | **str**|  | 
 **include** | **str**| Extra fields to include in the response | [optional] 

### Return type

[**OrgsorgidprojectsprojectidbuildtargetsBuilds**](OrgsorgidprojectsprojectidbuildtargetsBuilds.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

