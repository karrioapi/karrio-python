# Rate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique rate identifier | [optional] 
**carrier_name** | **str** | The rate&#39;s carrier | 
**carrier_id** | **str** | The targeted carrier&#39;s name (unique identifier) | 
**currency** | **str** | The rate monetary values currency code | 
**service** | **str** | The carrier&#39;s rate (quote) service | [optional] 
**discount** | **float** | The monetary amount of the discount on the rate | [optional] 
**base_charge** | **float** |  The rate&#39;s monetary amount of the base charge. This is the net amount of the rate before additional charges  | [optional] 
**total_charge** | **float** |  The rate&#39;s monetary amount of the total charge. This is the gross amount of the rate after adding the additional charges  | [optional] 
**duties_and_taxes** | **float** | The monetary amount of the duties and taxes if applied | [optional] 
**estimated_delivery** | **str** | The estimated delivery date | [optional] 
**extra_charges** | [**list[Charge]**](Charge.md) | list of the rate&#39;s additional charges | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


