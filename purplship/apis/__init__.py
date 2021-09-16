
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.api_api import APIApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from purplship.api.api_api import APIApi
from purplship.api.addresses_api import AddressesApi
from purplship.api.carriers_api import CarriersApi
from purplship.api.customs_api import CustomsApi
from purplship.api.parcels_api import ParcelsApi
from purplship.api.pickups_api import PickupsApi
from purplship.api.proxy_api import ProxyApi
from purplship.api.shipments_api import ShipmentsApi
from purplship.api.trackers_api import TrackersApi
from purplship.api.webhooks_api import WebhooksApi
