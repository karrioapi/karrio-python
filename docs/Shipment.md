# Shipment

The shipments associated with the order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcels** | [**[Parcel]**](Parcel.md) | The shipment&#39;s parcels | 
**created_at** | **str** |  The shipment creation datetime  Date Format: &#x60;YYYY-MM-DD HH:MM:SS.mmmmmmz&#x60;  | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**id** | **str** | A unique identifier | [optional] 
**object_type** | **str** | Specifies the object type | [optional]  if omitted the server will use the default value of "shipment"
**tracking_url** | **str, none_type** | The shipment tracking url | [optional] 
**services** | **[str], none_type** |  The carriers services requested for the shipment.  Please consult the reference for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  &lt;details&gt; &lt;summary&gt;The options available for the shipment.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;currency\&quot;: \&quot;USD\&quot;,     \&quot;insurance\&quot;: 100.00,     \&quot;cash_on_delivery\&quot;: 30.00,     \&quot;shipment_date\&quot;: \&quot;2020-01-01\&quot;,     \&quot;dangerous_good\&quot;: true,     \&quot;declared_value\&quot;: 150.00,     \&quot;email_notification\&quot;: true,     \&quot;email_notification_to\&quot;: \&quot;shipper@mail.com\&quot;,     \&quot;signature_confirmation\&quot;: true, } &#x60;&#x60;&#x60;  Please check the docs for carrier specific options. &lt;/details&gt;  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**rates** | [**[Rate]**](Rate.md) | The list for shipment rates fetched previously | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**label_type** | **str, none_type** | The shipment label file type. | [optional] 
**carrier_ids** | **[str], none_type** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 
**tracker_id** | **str, none_type** | The attached tracker id | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the shipment | [optional] 
**messages** | [**[Message]**](Message.md) | The list of note or warning messages | [optional] 
**status** | **str** | The current Shipment status | [optional]  if omitted the server will use the default value of "draft"
**carrier_name** | **str, none_type** | The shipment carrier | [optional] 
**carrier_id** | **str, none_type** | The shipment carrier configured identifier | [optional] 
**tracking_number** | **str, none_type** | The shipment tracking number | [optional] 
**shipment_identifier** | **str, none_type** | The shipment carrier system identifier | [optional] 
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | provider specific metadata | [optional] 
**service** | **str, none_type** | The selected service | [optional] 
**selected_rate_id** | **str, none_type** | The shipment selected rate. | [optional] 
**label_url** | **str, none_type** | The shipment label URL | [optional] 
**invoice_url** | **str, none_type** | The shipment invoice URL | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


