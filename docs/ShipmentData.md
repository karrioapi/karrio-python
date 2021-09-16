# ShipmentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**[ParcelData]**](ParcelData.md) | The shipment&#39;s parcels | 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  The options available for the shipment.&lt;br/&gt; Please consult [the reference](#operation/references) for additional specific carriers options.  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**reference** | **str, none_type** | The shipment reference | [optional] 
**label_type** | **str** | The shipment label file type. | [optional]  if omitted the server will use the default value of "PDF"
**services** | **[str], none_type** |  The requested carrier service for the shipment.  Please consult [the reference](#operation/references) for specific carriers services.&lt;br/&gt; Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**carrier_ids** | **[str], none_type** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


