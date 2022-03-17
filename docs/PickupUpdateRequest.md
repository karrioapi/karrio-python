# PickupUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_date** | **str** |  The expected pickup date  Date Format: &#x60;YYYY-MM-DD&#x60;  | 
**address** | [**Address**](Address.md) |  | 
**parcels** | [**[Parcel]**](Parcel.md) | The shipment parcels to pickup. | 
**confirmation_number** | **str** | pickup identification number | 
**ready_time** | **str** |  The ready time for pickup.  Time Format: &#x60;HH:MM&#x60;  | 
**closing_time** | **str** |  The closing or late time of the pickup  Time Format: &#x60;HH:MM&#x60;  | 
**instruction** | **str, none_type** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str, none_type** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Advanced carrier specific pickup options | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


