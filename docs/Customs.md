# Customs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier | [optional] 
**aes** | **str** |  | [optional] 
**eel_pfc** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content_description** | **str** |  | [optional] 
**incoterm** | **str** | The customs &#x27;term of trade&#x27; also known as &#x27;incoterm&#x27; | [optional] 
**commodities** | [**list[Commodity]**](Commodity.md) | The parcel content items | [optional] 
**duty** | [**Payment**](Payment.md) |  | [optional] 
**invoice** | **str** | The invoice reference number | [optional] 
**commercial_invoice** | **bool** | Indicates if the shipment is commercial | [optional] 
**certify** | **bool** | Indicate that signer certified confirmed all | [optional] 
**signer** | **str** |  | [optional] 
**certificate_number** | **str** |  | [optional] 
**options** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

