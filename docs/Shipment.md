# Shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier | [optional] 
**status** | **str** | The current Shipment status | [optional] [default to 'created']
**carrier_name** | **str** | The shipment carrier | [optional] 
**carrier_id** | **str** | The shipment carrier configured identifier | [optional] 
**label** | **str** | The shipment label in base64 string | [optional] 
**tracking_number** | **str** | The shipment tracking number | [optional] 
**shipment_identifier** | **str** | The shipment carrier system identifier | [optional] 
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 
**selected_rate_id** | **str** | The shipment selected rate. | [optional] 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | [optional] 
**tracking_url** | **str** | The shipment tracking url | [optional] 
**service** | **str** | The selected service | [optional] 
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcels** | [**list[Parcel]**](Parcel.md) | The shipment&#x27;s parcels | 
**services** | **list[str]** |  The carriers services requested for the shipment.  Please consult [the reference](#operation/references) for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **object** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 
**meta** | **object** | provider specific metadata | [optional] 
**created_at** | **str** |  The shipment creation date  Date Format: &#x60;YYYY-MM-DD&#x60;  | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**messages** | [**list[Message]**](Message.md) | The list of note or warning messages | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

