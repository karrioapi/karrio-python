# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from karrio.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from karrio.model.address import Address
from karrio.model.address_data import AddressData
from karrio.model.address_list import AddressList
from karrio.model.address_validation import AddressValidation
from karrio.model.carrier_list import CarrierList
from karrio.model.carrier_settings import CarrierSettings
from karrio.model.charge import Charge
from karrio.model.commodity import Commodity
from karrio.model.commodity_data import CommodityData
from karrio.model.customs import Customs
from karrio.model.customs_data import CustomsData
from karrio.model.customs_list import CustomsList
from karrio.model.documents import Documents
from karrio.model.duty import Duty
from karrio.model.error_response import ErrorResponse
from karrio.model.message import Message
from karrio.model.metadata import Metadata
from karrio.model.operation import Operation
from karrio.model.operation_confirmation import OperationConfirmation
from karrio.model.operation_response import OperationResponse
from karrio.model.order import Order
from karrio.model.order_data import OrderData
from karrio.model.order_list import OrderList
from karrio.model.order_update_data import OrderUpdateData
from karrio.model.parcel import Parcel
from karrio.model.parcel_data import ParcelData
from karrio.model.parcel_list import ParcelList
from karrio.model.payment import Payment
from karrio.model.pickup import Pickup
from karrio.model.pickup_cancel_data import PickupCancelData
from karrio.model.pickup_cancel_request import PickupCancelRequest
from karrio.model.pickup_data import PickupData
from karrio.model.pickup_list import PickupList
from karrio.model.pickup_request import PickupRequest
from karrio.model.pickup_response import PickupResponse
from karrio.model.pickup_update_data import PickupUpdateData
from karrio.model.pickup_update_request import PickupUpdateRequest
from karrio.model.rate import Rate
from karrio.model.rate_request import RateRequest
from karrio.model.rate_response import RateResponse
from karrio.model.references import References
from karrio.model.shipment import Shipment
from karrio.model.shipment_cancel_request import ShipmentCancelRequest
from karrio.model.shipment_data import ShipmentData
from karrio.model.shipment_list import ShipmentList
from karrio.model.shipment_purchase_data import ShipmentPurchaseData
from karrio.model.shipment_rate_data import ShipmentRateData
from karrio.model.shipment_update_data import ShipmentUpdateData
from karrio.model.shipping_request import ShippingRequest
from karrio.model.shipping_response import ShippingResponse
from karrio.model.token_obtain_pair import TokenObtainPair
from karrio.model.token_pair import TokenPair
from karrio.model.token_refresh import TokenRefresh
from karrio.model.token_verify import TokenVerify
from karrio.model.tracker_list import TrackerList
from karrio.model.tracking_event import TrackingEvent
from karrio.model.tracking_response import TrackingResponse
from karrio.model.tracking_status import TrackingStatus
from karrio.model.webhook import Webhook
from karrio.model.webhook_data import WebhookData
from karrio.model.webhook_list import WebhookList
from karrio.model.webhook_test_request import WebhookTestRequest
