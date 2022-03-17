# OrderData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The source&#39; order id. | 
**shipping_to** | [**AddressData**](AddressData.md) |  | 
**line_items** | [**[CommodityData]**](CommodityData.md) | The order line items. | 
**source** | **str** |  The order&#39;s source.  e.g. API, POS, ERP, Shopify, Woocommerce, etc.  | [optional]  if omitted the server will use the default value of "API"
**shipping_from** | [**AddressData**](AddressData.md) |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  &lt;details&gt; &lt;summary&gt;The options available for the order shipments.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;currency\&quot;: \&quot;USD\&quot;, } &#x60;&#x60;&#x60;  Please check the docs for shipment specific options. &lt;/details&gt;  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata for the order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


