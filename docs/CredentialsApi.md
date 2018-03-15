# swagger_client.CredentialsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credentials_android**](CredentialsApi.md#add_credentials_android) | **POST** /orgs/{orgid}/projects/{projectid}/credentials/signing/android | Upload Android Credentials
[**add_credentials_ios**](CredentialsApi.md#add_credentials_ios) | **POST** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios | Upload iOS Credentials
[**delete_android**](CredentialsApi.md#delete_android) | **DELETE** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Delete Android Credentials
[**delete_ios**](CredentialsApi.md#delete_ios) | **DELETE** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Delete iOS Credentials
[**get_all_android**](CredentialsApi.md#get_all_android) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/android | Get All Android Credentials
[**get_all_ios**](CredentialsApi.md#get_all_ios) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios | Get All iOS Credentials
[**get_one_android**](CredentialsApi.md#get_one_android) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Get Android Credential Details
[**get_one_ios**](CredentialsApi.md#get_one_ios) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Get iOS Credential Details
[**update_android**](CredentialsApi.md#update_android) | **PUT** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Update Android Credentials
[**update_ios**](CredentialsApi.md#update_ios) | **PUT** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Update iOS Credentials


# **add_credentials_android**
> InlineResponse20013 add_credentials_android(orgid, projectid, label, file, alias, keypass, storepass)

Upload Android Credentials

Upload a new android keystore for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
label = 'label_example' # str | Label for the uploaded credential
file = '/path/to/file.txt' # file | Keystore file
alias = 'alias_example' # str | Keystore alias
keypass = 'keypass_example' # str | Keystore keypass
storepass = 'storepass_example' # str | Keystore storepass

try: 
    # Upload Android Credentials
    api_response = api_instance.add_credentials_android(orgid, projectid, label, file, alias, keypass, storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **label** | **str**| Label for the uploaded credential | 
 **file** | **file**| Keystore file | 
 **alias** | **str**| Keystore alias | 
 **keypass** | **str**| Keystore keypass | 
 **storepass** | **str**| Keystore storepass | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_ios**
> InlineResponse20014 add_credentials_ios(orgid, projectid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)

Upload iOS Credentials

Upload a new iOS certificate and provisioning profile for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
label = 'label_example' # str | Label for the uploaded credentials
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try: 
    # Upload iOS Credentials
    api_response = api_instance.add_credentials_ios(orgid, projectid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **label** | **str**| Label for the uploaded credentials | 
 **file_certificate** | **file**| Certificate file (.p12) | 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_android**
> str delete_android(orgid, projectid, credentialid)

Delete Android Credentials

Delete specific android credentials for a project. NOTE: you must be a manager in the project's organization to delete credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try: 
    # Delete Android Credentials
    api_response = api_instance.delete_android(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ios**
> str delete_ios(orgid, projectid, credentialid)

Delete iOS Credentials

Delete specific ios credentials for a project. NOTE: you must be a manager in the project's organization to delete credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try: 
    # Delete iOS Credentials
    api_response = api_instance.delete_ios(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_android**
> list[InlineResponse20013] get_all_android(orgid, projectid)

Get All Android Credentials

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try: 
    # Get All Android Credentials
    api_response = api_instance.get_all_android(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ios**
> list[InlineResponse20014] get_all_ios(orgid, projectid)

Get All iOS Credentials

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try: 
    # Get All iOS Credentials
    api_response = api_instance.get_all_ios(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_android**
> InlineResponse20013 get_one_android(orgid, projectid, credentialid)

Get Android Credential Details

Get specific android credential details

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try: 
    # Get Android Credential Details
    api_response = api_instance.get_one_android(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_ios**
> InlineResponse20014 get_one_ios(orgid, projectid, credentialid)

Get iOS Credential Details

Get specific iOS credential details

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try: 
    # Get iOS Credential Details
    api_response = api_instance.get_one_ios(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_android**
> InlineResponse20013 update_android(orgid, projectid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)

Update Android Credentials

Update an android keystore for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the uploaded credential (optional)
file = '/path/to/file.txt' # file | Keystore file (optional)
alias = 'alias_example' # str | Keystore alias (optional)
keypass = 'keypass_example' # str | Keystore keypass (optional)
storepass = 'storepass_example' # str | Keystore storepass (optional)

try: 
    # Update Android Credentials
    api_response = api_instance.update_android(orgid, projectid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the uploaded credential | [optional] 
 **file** | **file**| Keystore file | [optional] 
 **alias** | **str**| Keystore alias | [optional] 
 **keypass** | **str**| Keystore keypass | [optional] 
 **storepass** | **str**| Keystore storepass | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ios**
> InlineResponse20014 update_ios(orgid, projectid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)

Update iOS Credentials

Update an iOS certificate / provisioning profile for the project. NOTE: you must be a manager in the project's organization to update credentials. 

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
# Configure OAuth2 access token for authorization: permissions
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CredentialsApi()
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the updated credentials (optional)
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12) (optional)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision) (optional)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try: 
    # Update iOS Credentials
    api_response = api_instance.update_ios(orgid, projectid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the updated credentials | [optional] 
 **file_certificate** | **file**| Certificate file (.p12) | [optional] 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | [optional] 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

