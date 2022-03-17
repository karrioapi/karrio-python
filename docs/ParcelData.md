# ParcelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | The parcel&#39;s weight | 
**weight_unit** | **str** | The parcel&#39;s weight unit | 
**width** | **float, none_type** | The parcel&#39;s width | [optional] 
**height** | **float, none_type** | The parcel&#39;s height | [optional] 
**length** | **float, none_type** | The parcel&#39;s length | [optional] 
**packaging_type** | **str, none_type** |  The parcel&#39;s packaging type.  **Note that the packaging is optional when using a package preset**  values: &lt;br/&gt; &#x60;envelope&#x60; &#x60;pak&#x60; &#x60;tube&#x60; &#x60;pallet&#x60; &#x60;small_box&#x60; &#x60;medium_box&#x60; &#x60;your_packaging&#x60;  For carrier specific packaging types, please consult the reference.  | [optional] 
**package_preset** | **str, none_type** |  The parcel&#39;s package preset.  For carrier specific package presets, please consult the reference.  | [optional] 
**description** | **str, none_type** | The parcel&#39;s description | [optional] 
**content** | **str, none_type** | The parcel&#39;s content description | [optional] 
**is_document** | **bool, none_type** | Indicates if the parcel is composed of documents only | [optional]  if omitted the server will use the default value of False
**dimension_unit** | **str, none_type** | The parcel&#39;s dimension unit | [optional] 
**items** | [**[CommodityData]**](CommodityData.md) | The parcel items. | [optional] 
**reference_number** | **str, none_type** | The parcel reference number. (can be used as tracking number for custom carriers) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


