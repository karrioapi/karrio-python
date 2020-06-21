# RateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**Address**](Address.md) |  | 
**recipient** | [**Address**](Address.md) |  | 
**parcel** | [**Parcel**](Parcel.md) |  | 
**services** | **list[str]** |  The requested carrier service for the shipment. Please consult [the reference](./UtilsApi.md#references) for specific carriers services.  Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


