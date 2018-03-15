# OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_export_method** | **str** | The fully-qualified name of a public static method you want us to call before we start the Unity build process. For example: ClassName.NeatMethod or NameSpace.ClassName.NeatMethod. No trailing parenthesis, and it can&#39;t have the same name as your Post-Export method! | [optional] 
**post_export_method** | **str** | The fully-qualified name of a public static method you want us to call after we finish the Unity build process (but before Xcode). For example: ClassName.CoolMethod or NameSpace.ClassName.CoolMethod. No trailing parenthesis, and it can&#39;t have the same name as your Post-Export method! This method must accept a string parameter, which will receive the path to the exported Unity player (or Xcode project in the case of iOS). | [optional] 
**pre_build_script** | **str** | Relative path to the script that should be run before the build process starts. | [optional] 
**post_build_script** | **str** | Relative path to the script that should be run after the build process finishes. | [optional] 
**scripting_define_symbols** | **str** | Enter the names of the symbols you want to define for iOS. These symbols can then be used as the conditions for #if directives just like the built-in ones. (i.e. #IF MYDEFINE or #IF AMAZON) | [optional] 
**player_exporter** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter**](OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter.md) |  | [optional] 
**player_settings** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerSettings**](OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerSettings.md) |  | [optional] 
**editor_user_build_settings** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityEditorUserBuildSettings**](OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityEditorUserBuildSettings.md) |  | [optional] 
**run_unit_tests** | **bool** | Run any unit tests your project has when a build happens. | [optional] 
**asset_bundles** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles**](OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.md) |  | [optional] 
**failed_unit_test_fails_build** | **bool** | Mark builds as failed if the unit tests do not pass. | [optional] 
**unit_test_method** | **str** | The Unity method to call when running unit tests. | [optional] 
**integration_test_method** | **str** | The Unity method to call when running integration tests. | [optional] 
**failed_integration_test_fails_build** | **bool** | Mark build as failed if integration tests do not pass. | [optional] 
**enable_light_bake** | **bool** | Enable lightmap baking (disabled by default since it is very slow and usually unnecessary) | [optional] 
**integration_test_scene_list** | **list[str]** | The collection of scenes to run integration tests within. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


