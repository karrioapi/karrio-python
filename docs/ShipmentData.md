# ShipmentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**list[ParcelData]**](ParcelData.md) | The shipment&#x27;s parcels | 
**options** | **object** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**payment** | [**PaymentData**](PaymentData.md) |  | [optional] 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional] [default to 'PDF']
**services** | **list[str]** |  The requested carrier service for the shipment.  Please consult [the reference](#operation/references) for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

