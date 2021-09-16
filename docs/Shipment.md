# Shipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcels** | [**[Parcel]**](Parcel.md) | The shipment&#39;s parcels | 
**created_at** | **str** |  The shipment creation datetime  Date Format: &#x60;YYYY-MM-DD HH:MM:SS.mmmmmmz&#x60;  | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**id** | **str** | A unique identifier | [optional] 
**status** | **str** | The current Shipment status | [optional]  if omitted the server will use the default value of "created"
**carrier_name** | **str, none_type** | The shipment carrier | [optional] 
**carrier_id** | **str, none_type** | The shipment carrier configured identifier | [optional] 
**label** | **str, none_type** | The shipment label in base64 string | [optional] 
**tracking_number** | **str, none_type** | The shipment tracking number | [optional] 
**shipment_identifier** | **str, none_type** | The shipment carrier system identifier | [optional] 
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 
**selected_rate_id** | **str, none_type** | The shipment selected rate. | [optional] 
**rates** | [**[Rate]**](Rate.md) | The list for shipment rates fetched previously | [optional] 
**tracking_url** | **str, none_type** | The shipment tracking url | [optional] 
**service** | **str, none_type** | The selected service | [optional] 
**services** | **[str], none_type** |  The carriers services requested for the shipment.  Please consult [the reference](#operation/references) for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**label_type** | **str, none_type** | The shipment label file type. | [optional] 
**carrier_ids** | **[str], none_type** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 
**tracker_id** | **str, none_type** | The attached tracker id | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | provider specific metadata | [optional] 
**messages** | [**[Message]**](Message.md) | The list of note or warning messages | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


