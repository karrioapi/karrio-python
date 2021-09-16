# Pickup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_name** | **str** | The pickup carrier | 
**carrier_id** | **str** | The pickup carrier configured name | 
**confirmation_number** | **str** | The pickup confirmation identifier | 
**address** | [**Address**](Address.md) |  | 
**parcels** | [**[Parcel], none_type**](Parcel.md) | The shipment parcels to pickup. | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**id** | **str** | A unique pickup identifier | [optional] 
**pickup_date** | **str, none_type** | The pickup date | [optional] 
**pickup_charge** | [**Charge**](Charge.md) |  | [optional] 
**ready_time** | **str, none_type** | The pickup expected ready time | [optional] 
**closing_time** | **str, none_type** | The pickup expected closing or late time | [optional] 
**instruction** | **str, none_type** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str, none_type** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Advanced carrier specific pickup options | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


