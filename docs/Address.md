# Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier | [optional] 
**postal_code** | **str** | The address postal code | [optional] 
**city** | **str** |  The address city. **(required to create as shipment)**  | [optional] 
**federal_tax_id** | **str** | The party frederal tax id | [optional] 
**state_tax_id** | **str** | The party state id | [optional] 
**person_name** | **str** |  attention to **(required to create as shipment)**  | [optional] 
**company_name** | **str** | The company name if the party is a company | [optional] 
**country_code** | **str** | The address country code | 
**email** | **str** | The party email | [optional] 
**phone_number** | **str** |  The party phone number.Note that the expected format is: **1 514 0000000**  Country Code | Area Code | Phone --- | --- | --- 1 | 514 | 0000000  | [optional] 
**state_code** | **str** | The address state code | [optional] 
**suburb** | **str** | The address suburb if known | [optional] 
**residential** | **bool** | Indicate if the address is residential or commercial (enterprise) | [optional] 
**address_line1** | **str** |  The address line with street number **(required to create as shipment)**  | [optional] 
**address_line2** | **str** | The address line with suite number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

