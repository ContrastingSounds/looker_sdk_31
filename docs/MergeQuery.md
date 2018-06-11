# MergeQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id | [optional] 
**pivots** | **list[str]** | Pivots | [optional] 
**sorts** | **list[str]** | Sorts | [optional] 
**column_limit** | **str** | Column Limit | [optional] 
**total** | **bool** | Total | [optional] 
**vis_config** | **dict(str, str)** | Visualization Config | [optional] 
**dynamic_fields** | **str** | Dynamic Fields | [optional] 
**source_queries** | [**list[MergeQuerySourceQuery]**](MergeQuerySourceQuery.md) | Source Queries defining the results to be merged. | [optional] 
**result_maker_id** | **int** | Unique to get results | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


