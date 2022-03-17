# CustomsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodities** | [**[CommodityData]**](CommodityData.md) | The parcel content items | 
**duty** | [**Duty**](Duty.md) |  | [optional] 
**content_type** | **str, none_type** |  | [optional] 
**content_description** | **str, none_type** |  | [optional] 
**incoterm** | **str, none_type** | The customs &#39;term of trade&#39; also known as &#39;incoterm&#39; | [optional] 
**invoice** | **str, none_type** | The invoice reference number | [optional] 
**invoice_date** | **str, none_type** | The invoice date | [optional] 
**commercial_invoice** | **bool, none_type** | Indicates if the shipment is commercial | [optional] 
**certify** | **bool, none_type** | Indicate that signer certified confirmed all | [optional] 
**signer** | **str, none_type** |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  &lt;details&gt; &lt;summary&gt;Customs identification options.&lt;/summary&gt;  &#x60;&#x60;&#x60; {     \&quot;aes\&quot;: \&quot;5218487281\&quot;,     \&quot;eel_pfc\&quot;: \&quot;5218487281\&quot;,     \&quot;license_number\&quot;: \&quot;5218487281\&quot;,     \&quot;certificate_number\&quot;: \&quot;5218487281\&quot;,     \&quot;nip_number\&quot;: \&quot;5218487281\&quot;,     \&quot;eori_number\&quot;: \&quot;5218487281\&quot;,     \&quot;vat_registration_number\&quot;: \&quot;5218487281\&quot;, } &#x60;&#x60;&#x60;  Please check the docs for carrier specific options. &lt;/details&gt;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


