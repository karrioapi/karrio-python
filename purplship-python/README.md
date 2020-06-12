# purplship
PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

```sh
pip install purplship
```

Then import the package:
```python
import purplship 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    configured_carriers = purplship.Carriers.retrieve()
    pprint(configured_carriers)
except ApiException as e:
    print("Exception when calling Carriers->retrieve: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://instance.purplship.api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Carriers* | [**retrieve**](docs/Carriers.md#retrieve) | **GET** /carriers | 
*Rates* | [**fetch**](docs/Rates.md#fetch) | **POST** /proxy/rates | 
*Shipments* | [**create**](docs/Shipments.md#create) | **POST** /proxy/shipments | 
*Tracking* | [**retrieve**](docs/Tracking.md#retrieve) | **GET** /proxy/tracking/{carrier_name}/{tracking_number} | 
*Utils* | [**get_reference**](docs/Utils.md#get_reference) | **GET** /references | 
*Utils* | [**print_label**](docs/Utils.md#print_label) | **POST** /labels | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [Card](docs/Card.md)
 - [CarrierSettings](docs/CarrierSettings.md)
 - [Charge](docs/Charge.md)
 - [Commodity](docs/Commodity.md)
 - [Customs](docs/Customs.md)
 - [Doc](docs/Doc.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Invoice](docs/Invoice.md)
 - [LabelPrintingRequest](docs/LabelPrintingRequest.md)
 - [Message](docs/Message.md)
 - [Parcel](docs/Parcel.md)
 - [Payment](docs/Payment.md)
 - [Rate](docs/Rate.md)
 - [RateRequest](docs/RateRequest.md)
 - [RateResponse](docs/RateResponse.md)
 - [References](docs/References.md)
 - [Shipment](docs/Shipment.md)
 - [ShipmentRequest](docs/ShipmentRequest.md)
 - [ShipmentResponse](docs/ShipmentResponse.md)
 - [TrackingDetails](docs/TrackingDetails.md)
 - [TrackingEvent](docs/TrackingEvent.md)
 - [TrackingResponse](docs/TrackingResponse.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

PurplShip Team | hello@purplship.com | [purplship.com](https://purplship.com)
