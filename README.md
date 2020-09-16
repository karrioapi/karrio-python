# purplship-python

Purplship is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services.

Visit [purplship.com](https://purplship.com) to deploy your private cloud multi-carrier shipping API instance.

## Documentation

See the full [Python API docs](https://docs.purplship.com).

## Requirements

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

### Usage

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
    print("Exception when calling purplship.Carriers->list: %s\n" % e)

```

## Author

PurplShip Team | hello@purplship.com | [purplship.com](https://purplship.com)
