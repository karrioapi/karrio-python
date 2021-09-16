# AddressData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The address country code | 
**postal_code** | **str, none_type** |  The address postal code  **(required for shipment purchase)**  | [optional] 
**city** | **str, none_type** |  The address city.  **(required for shipment purchase)**  | [optional] 
**federal_tax_id** | **str, none_type** | The party frederal tax id | [optional] 
**state_tax_id** | **str, none_type** | The party state id | [optional] 
**person_name** | **str, none_type** |  attention to  **(required for shipment purchase)**  | [optional] 
**company_name** | **str, none_type** | The company name if the party is a company | [optional] 
**email** | **str, none_type** | The party email | [optional] 
**phone_number** | **str, none_type** | The party phone number. | [optional] 
**state_code** | **str, none_type** | The address state code | [optional] 
**suburb** | **str, none_type** | The address suburb if known | [optional] 
**residential** | **bool, none_type** | Indicate if the address is residential or commercial (enterprise) | [optional]  if omitted the server will use the default value of False
**address_line1** | **str, none_type** |  The address line with street number &lt;br/&gt; **(required for shipment purchase)**  | [optional] 
**address_line2** | **str, none_type** | The address line with suite number | [optional] 
**validate_location** | **bool, none_type** | Indicate if the address should be validated | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


