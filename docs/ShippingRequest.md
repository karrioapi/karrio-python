# ShippingRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**list[ParcelData]**](ParcelData.md) | The shipment&#x27;s parcels | 
**options** | **object** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional] [default to 'PDF']
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**list[Rate]**](Rate.md) | The list for shipment rates fetched previously | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

