# purplship.Carriers

All URIs are relative to *https://instance.purplship.api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve**](Carriers.md#retrieve) | **GET** /carriers | 


# **retrieve**
> list[CarrierSettings] retrieve(carrier_name=carrier_name, carrier_id=carrier_id, test=test)



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

try:
    api_response = purplship.Carriers.retrieve(
        carrier_name='carrier_name_example',
        carrier_id='carrier_id_example',
        test=true
    )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Carriers->retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_name** | **str**| Indicates a carrier (type) | [optional] 
 **carrier_id** | **str**| Indicates a specific carrier configuration name. | [optional] 
 **test** | **bool**|  The test flag indicates whether to use a carrier configured for test.   | [optional] 

### Return type

[**list[CarrierSettings]**](CarrierSettings.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

