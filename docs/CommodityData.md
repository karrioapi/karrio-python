# CommodityData

The parcel content items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | The commodity&#39;s weight | 
**weight_unit** | **str** | The commodity&#39;s weight unit | 
**description** | **str, none_type** | A description of the commodity | [optional] 
**quantity** | **int** | The commodity&#39;s quantity (number or item) | [optional] 
**sku** | **str, none_type** | The commodity&#39;s sku number | [optional] 
**value_amount** | **float, none_type** | The monetary value of the commodity | [optional] 
**value_currency** | **str, none_type** | The currency of the commodity value amount | [optional] 
**origin_country** | **str, none_type** | The origin or manufacture country | [optional] 
**parent_id** | **str, none_type** | The id of the related order line item. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  &lt;details&gt; &lt;summary&gt;Commodity user references metadata.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;part_number\&quot;: \&quot;5218487281\&quot;,     \&quot;reference1\&quot;: \&quot;# ref 1\&quot;,     \&quot;reference2\&quot;: \&quot;# ref 2\&quot;,     \&quot;reference3\&quot;: \&quot;# ref 3\&quot;,     \&quot;reference4\&quot;: \&quot;# ref 4\&quot;,     ... } &#x60;&#x60;&#x60; &lt;/details&gt;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


