# purplship.Rate

All URIs are relative to *https://instance.purplship.api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch**](RateApi.md#fetch) | **POST** /proxy/rates | Fetch Shipment Rates


# **fetch**
> RateResponse fetch(data)

Fetch Shipment Rates

 The Shipping process begins by fetching rates for your shipment. The request returns rates required to create your shipment. 

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

data = purplship.RateRequest()

try:
    api_response = purplship.Rate.fetch(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Rate->fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RateRequest**](RateRequest.md)|  | 

### Return type

[**RateResponse**](RateResponse.md)

### Authorization

[Token](../README.md#Token), [OAuth2 password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

