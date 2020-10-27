# Pickup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique pickup identifier | [optional] 
**carrier_name** | **str** | The pickup carrier | 
**carrier_id** | **str** | The pickup carrier configured name | 
**confirmation_number** | **str** | The pickup confirmation identifier | 
**pickup_date** | **str** | The pickup date | [optional] 
**pickup_charge** | [**Charge**](Charge.md) |  | [optional] 
**ready_time** | **str** | The pickup expected ready time | [optional] 
**closing_time** | **str** | The pickup expected closing or late time | [optional] 
**address** | [**Address**](Address.md) |  | 
**parcels** | [**list[Parcel]**](Parcel.md) | The shipment parcels to pickup. | 
**instruction** | **str** |  The pickup instruction.  eg: Handle with care.  | [optional] 
**package_location** | **str** |  The package(s) location.  eg: Behind the entrance door.  | [optional] 
**options** | **object** | Advanced carrier specific pickup options | [optional] 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

