# ShippingRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**list[ParcelData]**](ParcelData.md) | The shipment&#x27;s parcels | 
**options** | **object** |  The options available for the shipment. Please consult the API reference for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**doc_images** | [**list[Doc]**](Doc.md) |  The list of documents to attach for a paperless interantional trade.  eg: Invoices...  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

