# ShippingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**[ParcelData]**](ParcelData.md) | The shipment&#39;s parcels | 
**payment** | [**Payment**](Payment.md) |  | 
**selected_rate_id** | **str** | The shipment selected rate. | 
**rates** | [**[Rate]**](Rate.md) | The list for shipment rates fetched previously | 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional]  if omitted the server will use the default value of "PDF"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


