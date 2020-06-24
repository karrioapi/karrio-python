# ShipmentRequest

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
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**list[Rate]**](RateApi.md) | The list for shipment rates fetched previously | 
**payment** | [**Payment**](Payment.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


