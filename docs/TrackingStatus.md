# TrackingStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier | [optional] 
**carrier_name** | **str** | The tracking carrier | 
**carrier_id** | **str** | The tracking carrier configured identifier | 
**tracking_number** | **str** | The shipment tracking number | 
**events** | [**list[TrackingEvent]**](TrackingEvent.md) | The tracking details events | [optional] 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

