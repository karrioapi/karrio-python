# Shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | 
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcel** | [**Parcel**](Parcel.md) |  | 
**services** | **list[str]** |  The requested carrier service for the shipment.  Please consult the reference for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **dict(str, str)** |  The options available for the shipment.&lt;br/&gt; Please consult the reference for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**doc_images** | [**list[Doc]**](Doc.md) |  The list of documents to attach for a paperless interantional trade.  eg: Invoices...  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**tracking_url** | **str** | The shipment tracking url | [optional] 
**id** | **str** | A unique shipment identifier | [optional] 
**carrier_name** | **str** | The shipment carrier | 
**carrier_id** | **str** | The shipment carrier configured identifier | 
**label** | **str** | The shipment label in base64 string | 
**tracking_number** | **str** | The shipment tracking number | 
**selected_rate** | [**Rate**](Rate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


