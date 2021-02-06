# purplship.ShipmentsApi

All URIs are relative to *https://app.purplship.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customs**](ShipmentsApi.md#add_customs) | **POST** /shipments/{id}/customs | Add shipment customs declaration
[**add_parcel**](ShipmentsApi.md#add_parcel) | **POST** /shipments/{id}/parcels | Add a parcel to a shipment
[**cancel**](ShipmentsApi.md#cancel) | **DELETE** /shipments/{id} | Cancel a shipment
[**create**](ShipmentsApi.md#create) | **POST** /shipments | Create a shipment
[**list**](ShipmentsApi.md#list) | **GET** /shipments | List all shipments
[**purchase**](ShipmentsApi.md#purchase) | **POST** /shipments/{id}/purchase | Buy a shipment label
[**rates**](ShipmentsApi.md#rates) | **GET** /shipments/{id}/rates | Fetch new shipment rates
[**retrieve**](ShipmentsApi.md#retrieve) | **GET** /shipments/{id} | Retrieve a shipment
[**set_options**](ShipmentsApi.md#set_options) | **POST** /shipments/{id}/options | Add shipment options

# **add_customs**
> Shipment add_customs(body, id)

Add shipment customs declaration

Add the customs declaration for the shipment if non existent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
body = purplship.CustomsData() # CustomsData | 
id = 'id_example' # str | 

try:
    # Add shipment customs declaration
    api_response = api_instance.add_customs(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->add_customs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomsData**](CustomsData.md)|  | 
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel**
> Shipment add_parcel(body, id)

Add a parcel to a shipment

Add a parcel to an existing shipment for a multi-parcel shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
body = purplship.ParcelData() # ParcelData | 
id = 'id_example' # str | 

try:
    # Add a parcel to a shipment
    api_response = api_instance.add_parcel(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->add_parcel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParcelData**](ParcelData.md)|  | 
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel**
> OperationResponse cancel(id)

Cancel a shipment

Void a shipment with the associated label.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Cancel a shipment
    api_response = api_instance.cancel(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Shipment create(body)

Create a shipment

Create a new shipment instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
body = purplship.ShipmentData() # ShipmentData | 

try:
    # Create a shipment
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentData**](ShipmentData.md)|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[Shipment] list(limit=limit, offset=offset)

List all shipments

Retrieve all shipments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List all shipments
    api_response = api_instance.list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Shipment]**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase**
> Shipment purchase(body, id)

Buy a shipment label

Select your preferred rates to buy a shipment label.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
body = purplship.ShipmentPurchaseData() # ShipmentPurchaseData | 
id = 'id_example' # str | 

try:
    # Buy a shipment label
    api_response = api_instance.purchase(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentPurchaseData**](ShipmentPurchaseData.md)|  | 
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rates**
> Shipment rates(id)

Fetch new shipment rates

Refresh the list of the shipment rates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Fetch new shipment rates
    api_response = api_instance.rates(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> Shipment retrieve(id)

Retrieve a shipment

Retrieve a shipment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieve a shipment
    api_response = api_instance.retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_options**
> Shipment set_options(body, id)

Add shipment options

Add one or many options to your shipment.<br/> **eg:**<br/> - add shipment **insurance** - specify the preferred transaction **currency** - setup a **cash collected on delivery** option  ```json {     \"insurance\": 120,     \"currency\": \"USD\" } ```  And many more, check additional options available in the [reference](#operation/all_references).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = purplship.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = purplship.ShipmentsApi(purplship.ApiClient(configuration))
body = NULL # object | 
id = 'id_example' # str | 

try:
    # Add shipment options
    api_response = api_instance.set_options(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentsApi->set_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

