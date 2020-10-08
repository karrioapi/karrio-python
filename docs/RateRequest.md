# RateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcels** | [**list[Parcel]**](Parcel.md) | The shipment&#x27;s parcels | 
**services** | **list[str]** |  The requested carrier service for the shipment. Please consult the API reference for specific carriers services.  Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | **object** |  The options available for the shipment.  Please consult the API reference for additional specific carriers options.  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

