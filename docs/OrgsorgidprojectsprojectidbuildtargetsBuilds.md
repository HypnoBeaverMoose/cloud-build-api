# OrgsorgidprojectsprojectidbuildtargetsBuilds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **float** |  | [optional] 
**buildtargetid** | **str** | unique id auto-generated from the build target name | [optional] 
**build_target_name** | **str** |  | [optional] 
**build_guid** | **str** | unique GUID identifying this build | [optional] 
**build_status** | **str** |  | [optional] 
**failure_details** | [**list[OrgsorgidprojectsprojectidbuildtargetsFailureDetails]**](OrgsorgidprojectsprojectidbuildtargetsFailureDetails.md) | list of failure details for this build attempt, when available | [optional] 
**canceled_by** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**workspace_size** | **float** | size of workspace in bytes | [optional] 
**created** | **str** | when the build was created | [optional] 
**finished** | **str** | when the build completely finished | [optional] 
**checkout_start_time** | **str** | when the build starting checking out code | [optional] 
**checkout_time_in_seconds** | **float** | amount of time spent checking out code | [optional] 
**build_start_time** | **str** | when the build started compiling | [optional] 
**build_time_in_seconds** | **float** | amount of time spend compiling | [optional] 
**publish_start_time** | **str** | when the build started saving build artifacts | [optional] 
**publish_time_in_seconds** | **float** | amount of time spent saving build artifacts | [optional] 
**total_time_in_seconds** | **float** | total time for the build | [optional] 
**last_built_revision** | **str** | source control commit id for the build | [optional] 
**changeset** | **list[object]** | a list of source control changes between this and the last build | [optional] 
**favorited** | **bool** | if the build is marked as do not delete or not | [optional] 
**label** | **str** | description given when a build is favorited | [optional] 
**deleted** | **bool** | if the build is deleted or not | [optional] 
**deleted_by** | **str** | email address of the user who deleted this attempt | [optional] 
**queued_reason** | **str** | reason the build is currently waiting | [optional] 
**cooldown_date** | **str** | time until this build will be reconsidered for building | [optional] 
**scm_branch** | **str** | scm branch to be built | [optional] 
**unity_version** | **str** | &#39;latest&#39; or a unity dot version with underscores (ex. &#39;4_6_5&#39;) | [optional] 
**xcode_version** | **str** | &#39;latest&#39; or a supported xcode version (ex. &#39;xcode7&#39;) | [optional] 
**audit_changes** | **float** |  | [optional] 
**project_version** | [**OrgsorgidprojectsprojectidbuildtargetsProjectVersion**](OrgsorgidprojectsprojectidbuildtargetsProjectVersion.md) |  | [optional] 
**project_name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**org_fk** | **str** |  | [optional] 
**links** | **object** |  | [optional] 
**test_results** | [**OrgsorgidprojectsprojectidbuildtargetsTestResults**](OrgsorgidprojectsprojectidbuildtargetsTestResults.md) |  | [optional] 
**error** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


