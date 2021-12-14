# purplship-python

Purplship is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services.

Visit [purplship.com](https://next.purplship.com) to deploy your private cloud multi-carrier shipping API instance.

## Documentation

See the full [Python API docs](https://next.purplship.com/docs/reference).

## Requirements

Python >= 3.6

## Installation & Usage

### pip install

```sh
pip install purplship-python
```

Then import the package:

```python
import purplship
```

### Usage

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import purplship
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
purplship.api_key = 'YOUR_API_KEY'
purplship.host = 'https://instance.purplship.api'

try:
    api_response = purplship.carriers.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling purplship.Carriers->list: %s\n" % e)

```

## Documentation For Models

 - [Address](docs/Address.md)
 - [AddressData](docs/AddressData.md)
 - [AddressList](docs/AddressList.md)
 - [AddressValidation](docs/AddressValidation.md)
 - [CarrierList](docs/CarrierList.md)
 - [CarrierSettings](docs/CarrierSettings.md)
 - [Charge](docs/Charge.md)
 - [Commodity](docs/Commodity.md)
 - [CommodityData](docs/CommodityData.md)
 - [Customs](docs/Customs.md)
 - [CustomsData](docs/CustomsData.md)
 - [CustomsList](docs/CustomsList.md)
 - [Duty](docs/Duty.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Message](docs/Message.md)
 - [Metadata](docs/Metadata.md)
 - [Operation](docs/Operation.md)
 - [OperationConfirmation](docs/OperationConfirmation.md)
 - [OperationResponse](docs/OperationResponse.md)
 - [Parcel](docs/Parcel.md)
 - [ParcelData](docs/ParcelData.md)
 - [ParcelList](docs/ParcelList.md)
 - [Payment](docs/Payment.md)
 - [Pickup](docs/Pickup.md)
 - [PickupCancelData](docs/PickupCancelData.md)
 - [PickupCancelRequest](docs/PickupCancelRequest.md)
 - [PickupData](docs/PickupData.md)
 - [PickupList](docs/PickupList.md)
 - [PickupRequest](docs/PickupRequest.md)
 - [PickupResponse](docs/PickupResponse.md)
 - [PickupUpdateData](docs/PickupUpdateData.md)
 - [PickupUpdateRequest](docs/PickupUpdateRequest.md)
 - [Rate](docs/Rate.md)
 - [RateRequest](docs/RateRequest.md)
 - [RateResponse](docs/RateResponse.md)
 - [References](docs/References.md)
 - [Shipment](docs/Shipment.md)
 - [ShipmentCancelRequest](docs/ShipmentCancelRequest.md)
 - [ShipmentData](docs/ShipmentData.md)
 - [ShipmentList](docs/ShipmentList.md)
 - [ShipmentPurchaseData](docs/ShipmentPurchaseData.md)
 - [ShipmentRateData](docs/ShipmentRateData.md)
 - [ShippingRequest](docs/ShippingRequest.md)
 - [TokenObtainPair](docs/TokenObtainPair.md)
 - [TokenPair](docs/TokenPair.md)
 - [TokenRefresh](docs/TokenRefresh.md)
 - [TokenVerify](docs/TokenVerify.md)
 - [TrackerList](docs/TrackerList.md)
 - [TrackingEvent](docs/TrackingEvent.md)
 - [TrackingResponse](docs/TrackingResponse.md)
 - [TrackingStatus](docs/TrackingStatus.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookData](docs/WebhookData.md)
 - [WebhookList](docs/WebhookList.md)
 - [WebhookTestRequest](docs/WebhookTestRequest.md)

## Author

Purplship Team | hello@purplship.com | [purplship.com](https://purplship.com)
