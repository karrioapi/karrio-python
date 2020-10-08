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
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 
**selected_rate_id** | **str** | The shipment selected rate. | [optional] 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | [optional] 
**tracking_url** | **str** | The shipment tracking url | [optional] 
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcels** | [**list[Parcel]**](Parcel.md) | The shipment&#x27;s parcels | 
**services** | **list[str]** |  The requested carrier service for the shipment.  Please consult the API reference for specific carriers services. Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **object** |  The options available for the shipment. Please consult the API reference for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**doc_images** | [**list[Doc]**](Doc.md) |  The list of documents to attach for a paperless interantional trade.  eg: Invoices...  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 
**meta** | **object** | provider specific metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

