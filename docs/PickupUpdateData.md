# PickupUpdateData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_number** | **str** | pickup identification number | 
**pickup_date** | **str** |  The expected pickup date  Date Format: YYYY-MM-DD  | [optional] 
**address** | [**AddressData**](AddressData.md) |  | [optional] 
**ready_time** | **str, none_type** | The ready time for pickup. | [optional] 
**closing_time** | **str, none_type** | The closing or late time of the pickup | [optional] 
**instruction** | **str, none_type** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str, none_type** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Advanced carrier specific pickup options | [optional] 
**tracking_numbers** | **[str]** | The list of shipments to be picked up | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the pickup | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


