# Webhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the webhook endpoint. | 
**enabled_events** | **[str]** | The list of events to enable for this endpoint. | 
**test_mode** | **bool** | Specified whether it was created with a carrier in test mode | 
**secret** | **str** | Header signature secret | 
**id** | **str** | A unique identifier | [optional] 
**description** | **str, none_type** | An optional description of what the webhook is used for. | [optional] 
**disabled** | **bool, none_type** | Indicates that the webhook is disabled | [optional] 
**object_type** | **str** | Specifies the object type | [optional]  if omitted the server will use the default value of "webhook"
**last_event_at** | **datetime, none_type** | The datetime of the last event sent. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


