# ParcelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | The parcel&#39;s weight | 
**weight_unit** | **str** | The parcel&#39;s weight unit | 
**width** | **float, none_type** | The parcel&#39;s width | [optional] 
**height** | **float, none_type** | The parcel&#39;s height | [optional] 
**length** | **float, none_type** | The parcel&#39;s length | [optional] 
**packaging_type** | **str, none_type** |  The parcel&#39;s packaging type.  **Note that the packaging is optional when using a package preset**  values: &lt;br/&gt;- **envelope**&lt;br/&gt;- **pak**&lt;br/&gt;- **tube**&lt;br/&gt;- **pallet**&lt;br/&gt;- **small_box**&lt;br/&gt;- **medium_box**&lt;br/&gt;- **your_packaging**  For specific carriers packaging type, please consult [the reference](#operation/references).  | [optional] 
**package_preset** | **str, none_type** |  The parcel&#39;s package preset.  For specific carriers package preset, please consult [the reference](#operation/references).  | [optional] 
**description** | **str, none_type** | The parcel&#39;s description | [optional] 
**content** | **str, none_type** | The parcel&#39;s content description | [optional] 
**is_document** | **bool, none_type** | Indicates if the parcel is composed of documents only | [optional]  if omitted the server will use the default value of False
**dimension_unit** | **str, none_type** | The parcel&#39;s dimension unit | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


