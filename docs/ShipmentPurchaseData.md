# ShipmentPurchaseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_rate_id** | **str** | The shipment selected rate. | 
**label_type** | **str** | The shipment label file type. | [optional]  if omitted the server will use the default value of "PDF"
**payment** | [**Payment**](Payment.md) |  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the shipment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


