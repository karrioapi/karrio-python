# purplship

PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services.

Visit [purplship.com](https://purplship.com) to deploy your private cloud multi-carrier shipping API instance.

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

```sh
pip install purplship-python
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
    api_response = purplship.Carriers.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Carriers->list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://instance.purplship.api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Carriers* | [**list**](docs/CarriersApi.md#list) | **GET** /carriers | List all Carriers
*Carriers* | [**retrieve**](docs/CarriersApi.md#retrieve) | **GET** /carriers/{carrier_id_or_pk} | Retrieve a Carrier
*Rate* | [**fetch**](docs/RateApi.md#fetch) | **POST** /proxy/rates | Fetch Shipment Rates
*Shipment* | [**create**](docs/ShipmentApi.md#shipment) | **POST** /proxy/shipments | Create a Shipment
*Tracking* | [**fetch**](docs/TrackingApi.md#fetch) | **GET** /proxy/tracking/{carrier_name}/{tracking_number} | Track a Shipment
*Utils* | [**references**](docs/UtilsApi.md#references) | **GET** /references | Get all References
*Utils* | [**print_label**](docs/UtilsApi.md#print_label) | **POST** /labels | Print a Label


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
 - [Options](docs/Options.md)
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

## OAuth2 password

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **read**: Read everything.
 - **write**: Write everything,


## Author

PurplShip Team | hello@purplship.com | [purplship.com](https://purplship.com)
