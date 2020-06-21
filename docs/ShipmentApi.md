# purplship.Shipment

All URIs are relative to *https://instance.purplship.api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ShipmentApi.md#create) | **POST** /proxy/shipments | Create a Shipment


# **create**
> ShipmentResponse create(data)

Create a Shipment

 Once a Shipment is initialized by fetching the rates, the remaining requirements might be specified  to submit the shipment to the carrier of the selected rate of your choice. 

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

data = purplship.models.ShipmentRequest()

try:
    api_response = purplship.Shipment.create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Shipment->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ShipmentRequest**](ShipmentRequest.md)|  | 

### Return type

[**ShipmentResponse**](ShipmentResponse.md)

### Authorization

[Token](../README.md#Token), [OAuth2 password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

