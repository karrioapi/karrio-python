# purplship.Carriers

All URIs are relative to *https://instance.purplship.api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CarriersApi.md#list) | **GET** /carriers | List all Carriers
[**retrieve**](CarriersApi.md#retrieve) | **GET** /carriers/{carrier_id_or_pk} | Retrieve a Carrier


# **list**
> list[CarrierSettings] list(carrier_name=carrier_name, test=test)

List all Carriers

Returns the list of configured carriers

### Example
```python
from __future__ import print_function
import time
import purplship
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
purplship.api_key = 'YOUR_API_KEY'
purplship.host = 'https://instance.purplship.api/v1'

carrier_name = 'carrier_name_example' 
test = true

try:
    api_response = purplship.Carriers.list(carrier_name=carrier_name, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Carriers->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_name** | **str**| Indicates a carrier (type) | [optional] 
 **test** | **bool**| The test flag filter carrier configured in test mode | [optional] 

### Return type

[**list[CarrierSettings]**](CarrierSettings.md)

### Authorization

[Token](../README.md#Token), [OAuth2 password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> CarrierSettings retrieve(carrier_id_or_pk)

Retrieve a Carrier

Retrieve a configured carrier instance.

### Example
```python
from __future__ import print_function
import time
import purplship
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
purplship.api_key = 'YOUR_API_KEY'
purplship.host = 'https://instance.purplship.api/v1'

carrier_id_or_pk = 'carrier_id_or_pk_example'

try:
    api_response = purplship.Carriers.retrieve(carrier_id_or_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Carriers->retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_id_or_pk** | **str**|  | 

### Return type

[**CarrierSettings**](CarrierSettings.md)

### Authorization

[Token](../README.md#Token), [OAuth2 password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

