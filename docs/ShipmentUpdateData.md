# ShipmentUpdateData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_type** | **str** | The shipment label file type. | [optional]  if omitted the server will use the default value of "PDF"
**payment** | [**Payment**](Payment.md) |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  &lt;details&gt; &lt;summary&gt;The options available for the shipment.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;currency\&quot;: \&quot;USD\&quot;,     \&quot;insurance\&quot;: 100.00,     \&quot;cash_on_delivery\&quot;: 30.00,     \&quot;shipment_date\&quot;: \&quot;2020-01-01\&quot;,     \&quot;dangerous_good\&quot;: true,     \&quot;declared_value\&quot;: 150.00,     \&quot;email_notification\&quot;: true,     \&quot;email_notification_to\&quot;: \&quot;shipper@mail.com\&quot;,     \&quot;signature_confirmation\&quot;: true, } &#x60;&#x60;&#x60;  Please check the docs for carrier specific options. &lt;/details&gt;  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the shipment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


