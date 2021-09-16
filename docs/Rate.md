# Rate

The list of returned rates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_name** | **str** | The rate&#39;s carrier | 
**carrier_id** | **str** | The targeted carrier&#39;s name (unique identifier) | 
**currency** | **str** | The rate monetary values currency code | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**id** | **str** | A unique identifier | [optional] 
**service** | **str, none_type** | The carrier&#39;s rate (quote) service | [optional] 
**discount** | **float, none_type** | The monetary amount of the discount on the rate | [optional] 
**base_charge** | **float** |  The rate&#39;s monetary amount of the base charge.&lt;br/&gt; This is the net amount of the rate before additional charges  | [optional] 
**total_charge** | **float** |  The rate&#39;s monetary amount of the total charge.&lt;br/&gt; This is the gross amount of the rate after adding the additional charges  | [optional] 
**duties_and_taxes** | **float, none_type** | The monetary amount of the duties and taxes if applied | [optional] 
**transit_days** | **int, none_type** | The estimated delivery transit days | [optional] 
**extra_charges** | [**[Charge]**](Charge.md) | list of the rate&#39;s additional charges | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | provider specific metadata | [optional] 
**carrier_ref** | **str, none_type** | The system carrier configuration id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


