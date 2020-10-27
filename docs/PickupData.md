# PickupData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_date** | **str** |  The expected pickup date  Date Format: YYYY-MM-DD  | 
**address** | [**AddressData**](AddressData.md) |  | [optional] 
**ready_time** | **str** | The ready time for pickup. | 
**closing_time** | **str** | The closing or late time of the pickup | 
**instruction** | **str** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **object** | Advanced carrier specific pickup options | [optional] 
**tracking_numbers** | **list[str]** | The list of shipments to be picked up | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

