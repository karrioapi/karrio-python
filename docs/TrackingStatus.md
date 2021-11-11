# TrackingStatus

The tracking details retrieved

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_name** | **str** | The tracking carrier | 
**carrier_id** | **str** | The tracking carrier configured identifier | 
**tracking_number** | **str** | The shipment tracking number | 
**test_mode** | **bool** | Specified whether the object was created with a carrier in test mode | 
**id** | **str** | A unique identifier | [optional] 
**events** | [**[TrackingEvent], none_type**](TrackingEvent.md) | The tracking details events | [optional] 
**delivered** | **bool** | Specified whether the related shipment was delivered | [optional] 
**status** | **str** | The current tracking status | [optional]  if omitted the server will use the default value of "pending"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


