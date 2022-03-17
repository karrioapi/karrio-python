# Order


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The source&#39; order id. | 
**shipping_to** | [**Address**](Address.md) |  | 
**line_items** | [**[Commodity]**](Commodity.md) | The order line items. | 
**test_mode** | **bool** | Specify whether the order is in test mode or not. | 
**created_at** | **str** |  The shipment creation datetime  Date Format: &#x60;YYYY-MM-DD HH:MM:SS.mmmmmmz&#x60;  | 
**id** | **str** | A unique identifier | [optional] 
**object_type** | **str** | Specifies the object type | [optional]  if omitted the server will use the default value of "order"
**source** | **str** | The order&#39;s source. | [optional] 
**status** | **str** | The order status. | [optional]  if omitted the server will use the default value of "unfulfilled"
**shipping_from** | [**Address**](Address.md) |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  &lt;details&gt; &lt;summary&gt;The options available for the order shipments.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;currency\&quot;: \&quot;USD\&quot;, } &#x60;&#x60;&#x60;  Please check the docs for shipment specific options. &lt;/details&gt;  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the order. | [optional] 
**shipments** | [**[Shipment]**](Shipment.md) | The shipments associated with the order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


