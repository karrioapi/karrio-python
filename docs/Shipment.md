# Shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcel** | [**Parcel**](Parcel.md) |  | 
**services** | **list[str]** |  The requested carrier service for the shipment.  Please consult [the reference](./UtilsApi.md#references) for specific carriers services. Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**doc_images** | [**list[Doc]**](Doc.md) |  The list of documents to attach for a paperless interantional trade.  eg: Invoices...  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**id** | **str** | A unique shipment identifier | [optional] 
**carrier_name** | **str** | The shipment carrier | [optional] 
**carrier_id** | **str** | The shipment carrier configured identifier | [optional] 
**label** | **str** | The shipment label in base64 string | [optional] 
**tracking_number** | **str** | The shipment tracking number | [optional] 
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**selected_rate_id** | **str** | The shipment selected rate. | [optional] 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | [optional] 
**tracking_url** | **str** | The shipment tracking url | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


