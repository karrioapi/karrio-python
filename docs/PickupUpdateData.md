# PickupUpdateData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_date** | **str** |  The expected pickup date  Date Format: YYYY-MM-DD  | [optional] 
**address** | [**AddressData**](AddressData.md) |  | [optional] 
**ready_time** | **str** | The ready time for pickup. | [optional] 
**closing_time** | **str** | The closing or late time of the pickup | [optional] 
**instruction** | **str** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **object** | Advanced carrier specific pickup options | [optional] 
**tracking_numbers** | **list[str]** | The list of shipments to be picked up | [optional] 
**confirmation_number** | **str** | pickup identification number | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

