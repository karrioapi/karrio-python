# ShippingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**[ParcelData]**](ParcelData.md) | The shipment&#39;s parcels | 
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**[Rate]**](Rate.md) | The list for shipment rates fetched previously | 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  &lt;details&gt; &lt;summary&gt;The options available for the shipment.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;currency\&quot;: \&quot;USD\&quot;,     \&quot;insurance\&quot;: 100.00,     \&quot;cash_on_delivery\&quot;: 30.00,     \&quot;shipment_date\&quot;: \&quot;2020-01-01\&quot;,     \&quot;dangerous_good\&quot;: true,     \&quot;declared_value\&quot;: 150.00,     \&quot;email_notification\&quot;: true,     \&quot;email_notification_to\&quot;: \&quot;shipper@mail.com\&quot;,     \&quot;signature_confirmation\&quot;: true, } &#x60;&#x60;&#x60;  Please check the docs for carrier specific options. &lt;/details&gt;  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional]  if omitted the server will use the default value of "PDF"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


