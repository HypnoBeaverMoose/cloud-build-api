# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ``` 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2006Effective(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'label': 'str',
        'num_projects': 'float',
        'concurrent_builds': 'float',
        'cooldown_minutes': 'float',
        'cooldown_grace_period_minutes': 'float',
        'collaborators': 'float',
        'repo_size_limit_mb': 'float',
        'repo_size_limit_threshold_mb': 'float',
        'download_limit_mb': 'float',
        'build_manifest': 'bool',
        'library_caching': 'bool',
        'push_external_services': 'bool',
        'support_tickets': 'bool',
        'api_access': 'bool',
        'scheduled_builds': 'bool',
        'workspace_caching': 'bool',
        'checkout_method_override': 'str',
        'building_disabled': 'bool',
        'advanced_features': 'list[str]',
        'scm_types': 'list[str]'
    }

    attribute_map = {
        'label': 'label',
        'num_projects': 'numProjects',
        'concurrent_builds': 'concurrentBuilds',
        'cooldown_minutes': 'cooldownMinutes',
        'cooldown_grace_period_minutes': 'cooldownGracePeriodMinutes',
        'collaborators': 'collaborators',
        'repo_size_limit_mb': 'repoSizeLimitMB',
        'repo_size_limit_threshold_mb': 'repoSizeLimitThresholdMB',
        'download_limit_mb': 'downloadLimitMB',
        'build_manifest': 'buildManifest',
        'library_caching': 'libraryCaching',
        'push_external_services': 'pushExternalServices',
        'support_tickets': 'supportTickets',
        'api_access': 'apiAccess',
        'scheduled_builds': 'scheduledBuilds',
        'workspace_caching': 'workspaceCaching',
        'checkout_method_override': 'checkoutMethodOverride',
        'building_disabled': 'buildingDisabled',
        'advanced_features': 'advancedFeatures',
        'scm_types': 'scmTypes'
    }

    def __init__(self, label=None, num_projects=None, concurrent_builds=None, cooldown_minutes=None, cooldown_grace_period_minutes=None, collaborators=None, repo_size_limit_mb=None, repo_size_limit_threshold_mb=None, download_limit_mb=None, build_manifest=None, library_caching=None, push_external_services=None, support_tickets=None, api_access=None, scheduled_builds=None, workspace_caching=None, checkout_method_override=None, building_disabled=None, advanced_features=None, scm_types=None):
        """
        InlineResponse2006Effective - a model defined in Swagger
        """

        self._label = None
        self._num_projects = None
        self._concurrent_builds = None
        self._cooldown_minutes = None
        self._cooldown_grace_period_minutes = None
        self._collaborators = None
        self._repo_size_limit_mb = None
        self._repo_size_limit_threshold_mb = None
        self._download_limit_mb = None
        self._build_manifest = None
        self._library_caching = None
        self._push_external_services = None
        self._support_tickets = None
        self._api_access = None
        self._scheduled_builds = None
        self._workspace_caching = None
        self._checkout_method_override = None
        self._building_disabled = None
        self._advanced_features = None
        self._scm_types = None

        if label is not None:
          self.label = label
        if num_projects is not None:
          self.num_projects = num_projects
        if concurrent_builds is not None:
          self.concurrent_builds = concurrent_builds
        if cooldown_minutes is not None:
          self.cooldown_minutes = cooldown_minutes
        if cooldown_grace_period_minutes is not None:
          self.cooldown_grace_period_minutes = cooldown_grace_period_minutes
        if collaborators is not None:
          self.collaborators = collaborators
        if repo_size_limit_mb is not None:
          self.repo_size_limit_mb = repo_size_limit_mb
        if repo_size_limit_threshold_mb is not None:
          self.repo_size_limit_threshold_mb = repo_size_limit_threshold_mb
        if download_limit_mb is not None:
          self.download_limit_mb = download_limit_mb
        if build_manifest is not None:
          self.build_manifest = build_manifest
        if library_caching is not None:
          self.library_caching = library_caching
        if push_external_services is not None:
          self.push_external_services = push_external_services
        if support_tickets is not None:
          self.support_tickets = support_tickets
        if api_access is not None:
          self.api_access = api_access
        if scheduled_builds is not None:
          self.scheduled_builds = scheduled_builds
        if workspace_caching is not None:
          self.workspace_caching = workspace_caching
        if checkout_method_override is not None:
          self.checkout_method_override = checkout_method_override
        if building_disabled is not None:
          self.building_disabled = building_disabled
        if advanced_features is not None:
          self.advanced_features = advanced_features
        if scm_types is not None:
          self.scm_types = scm_types

    @property
    def label(self):
        """
        Gets the label of this InlineResponse2006Effective.

        :return: The label of this InlineResponse2006Effective.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this InlineResponse2006Effective.

        :param label: The label of this InlineResponse2006Effective.
        :type: str
        """

        self._label = label

    @property
    def num_projects(self):
        """
        Gets the num_projects of this InlineResponse2006Effective.

        :return: The num_projects of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._num_projects

    @num_projects.setter
    def num_projects(self, num_projects):
        """
        Sets the num_projects of this InlineResponse2006Effective.

        :param num_projects: The num_projects of this InlineResponse2006Effective.
        :type: float
        """

        self._num_projects = num_projects

    @property
    def concurrent_builds(self):
        """
        Gets the concurrent_builds of this InlineResponse2006Effective.

        :return: The concurrent_builds of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._concurrent_builds

    @concurrent_builds.setter
    def concurrent_builds(self, concurrent_builds):
        """
        Sets the concurrent_builds of this InlineResponse2006Effective.

        :param concurrent_builds: The concurrent_builds of this InlineResponse2006Effective.
        :type: float
        """

        self._concurrent_builds = concurrent_builds

    @property
    def cooldown_minutes(self):
        """
        Gets the cooldown_minutes of this InlineResponse2006Effective.

        :return: The cooldown_minutes of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._cooldown_minutes

    @cooldown_minutes.setter
    def cooldown_minutes(self, cooldown_minutes):
        """
        Sets the cooldown_minutes of this InlineResponse2006Effective.

        :param cooldown_minutes: The cooldown_minutes of this InlineResponse2006Effective.
        :type: float
        """

        self._cooldown_minutes = cooldown_minutes

    @property
    def cooldown_grace_period_minutes(self):
        """
        Gets the cooldown_grace_period_minutes of this InlineResponse2006Effective.

        :return: The cooldown_grace_period_minutes of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._cooldown_grace_period_minutes

    @cooldown_grace_period_minutes.setter
    def cooldown_grace_period_minutes(self, cooldown_grace_period_minutes):
        """
        Sets the cooldown_grace_period_minutes of this InlineResponse2006Effective.

        :param cooldown_grace_period_minutes: The cooldown_grace_period_minutes of this InlineResponse2006Effective.
        :type: float
        """

        self._cooldown_grace_period_minutes = cooldown_grace_period_minutes

    @property
    def collaborators(self):
        """
        Gets the collaborators of this InlineResponse2006Effective.

        :return: The collaborators of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """
        Sets the collaborators of this InlineResponse2006Effective.

        :param collaborators: The collaborators of this InlineResponse2006Effective.
        :type: float
        """

        self._collaborators = collaborators

    @property
    def repo_size_limit_mb(self):
        """
        Gets the repo_size_limit_mb of this InlineResponse2006Effective.

        :return: The repo_size_limit_mb of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._repo_size_limit_mb

    @repo_size_limit_mb.setter
    def repo_size_limit_mb(self, repo_size_limit_mb):
        """
        Sets the repo_size_limit_mb of this InlineResponse2006Effective.

        :param repo_size_limit_mb: The repo_size_limit_mb of this InlineResponse2006Effective.
        :type: float
        """

        self._repo_size_limit_mb = repo_size_limit_mb

    @property
    def repo_size_limit_threshold_mb(self):
        """
        Gets the repo_size_limit_threshold_mb of this InlineResponse2006Effective.

        :return: The repo_size_limit_threshold_mb of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._repo_size_limit_threshold_mb

    @repo_size_limit_threshold_mb.setter
    def repo_size_limit_threshold_mb(self, repo_size_limit_threshold_mb):
        """
        Sets the repo_size_limit_threshold_mb of this InlineResponse2006Effective.

        :param repo_size_limit_threshold_mb: The repo_size_limit_threshold_mb of this InlineResponse2006Effective.
        :type: float
        """

        self._repo_size_limit_threshold_mb = repo_size_limit_threshold_mb

    @property
    def download_limit_mb(self):
        """
        Gets the download_limit_mb of this InlineResponse2006Effective.

        :return: The download_limit_mb of this InlineResponse2006Effective.
        :rtype: float
        """
        return self._download_limit_mb

    @download_limit_mb.setter
    def download_limit_mb(self, download_limit_mb):
        """
        Sets the download_limit_mb of this InlineResponse2006Effective.

        :param download_limit_mb: The download_limit_mb of this InlineResponse2006Effective.
        :type: float
        """

        self._download_limit_mb = download_limit_mb

    @property
    def build_manifest(self):
        """
        Gets the build_manifest of this InlineResponse2006Effective.

        :return: The build_manifest of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._build_manifest

    @build_manifest.setter
    def build_manifest(self, build_manifest):
        """
        Sets the build_manifest of this InlineResponse2006Effective.

        :param build_manifest: The build_manifest of this InlineResponse2006Effective.
        :type: bool
        """

        self._build_manifest = build_manifest

    @property
    def library_caching(self):
        """
        Gets the library_caching of this InlineResponse2006Effective.

        :return: The library_caching of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._library_caching

    @library_caching.setter
    def library_caching(self, library_caching):
        """
        Sets the library_caching of this InlineResponse2006Effective.

        :param library_caching: The library_caching of this InlineResponse2006Effective.
        :type: bool
        """

        self._library_caching = library_caching

    @property
    def push_external_services(self):
        """
        Gets the push_external_services of this InlineResponse2006Effective.

        :return: The push_external_services of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._push_external_services

    @push_external_services.setter
    def push_external_services(self, push_external_services):
        """
        Sets the push_external_services of this InlineResponse2006Effective.

        :param push_external_services: The push_external_services of this InlineResponse2006Effective.
        :type: bool
        """

        self._push_external_services = push_external_services

    @property
    def support_tickets(self):
        """
        Gets the support_tickets of this InlineResponse2006Effective.

        :return: The support_tickets of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._support_tickets

    @support_tickets.setter
    def support_tickets(self, support_tickets):
        """
        Sets the support_tickets of this InlineResponse2006Effective.

        :param support_tickets: The support_tickets of this InlineResponse2006Effective.
        :type: bool
        """

        self._support_tickets = support_tickets

    @property
    def api_access(self):
        """
        Gets the api_access of this InlineResponse2006Effective.

        :return: The api_access of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._api_access

    @api_access.setter
    def api_access(self, api_access):
        """
        Sets the api_access of this InlineResponse2006Effective.

        :param api_access: The api_access of this InlineResponse2006Effective.
        :type: bool
        """

        self._api_access = api_access

    @property
    def scheduled_builds(self):
        """
        Gets the scheduled_builds of this InlineResponse2006Effective.

        :return: The scheduled_builds of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._scheduled_builds

    @scheduled_builds.setter
    def scheduled_builds(self, scheduled_builds):
        """
        Sets the scheduled_builds of this InlineResponse2006Effective.

        :param scheduled_builds: The scheduled_builds of this InlineResponse2006Effective.
        :type: bool
        """

        self._scheduled_builds = scheduled_builds

    @property
    def workspace_caching(self):
        """
        Gets the workspace_caching of this InlineResponse2006Effective.

        :return: The workspace_caching of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._workspace_caching

    @workspace_caching.setter
    def workspace_caching(self, workspace_caching):
        """
        Sets the workspace_caching of this InlineResponse2006Effective.

        :param workspace_caching: The workspace_caching of this InlineResponse2006Effective.
        :type: bool
        """

        self._workspace_caching = workspace_caching

    @property
    def checkout_method_override(self):
        """
        Gets the checkout_method_override of this InlineResponse2006Effective.

        :return: The checkout_method_override of this InlineResponse2006Effective.
        :rtype: str
        """
        return self._checkout_method_override

    @checkout_method_override.setter
    def checkout_method_override(self, checkout_method_override):
        """
        Sets the checkout_method_override of this InlineResponse2006Effective.

        :param checkout_method_override: The checkout_method_override of this InlineResponse2006Effective.
        :type: str
        """

        self._checkout_method_override = checkout_method_override

    @property
    def building_disabled(self):
        """
        Gets the building_disabled of this InlineResponse2006Effective.

        :return: The building_disabled of this InlineResponse2006Effective.
        :rtype: bool
        """
        return self._building_disabled

    @building_disabled.setter
    def building_disabled(self, building_disabled):
        """
        Sets the building_disabled of this InlineResponse2006Effective.

        :param building_disabled: The building_disabled of this InlineResponse2006Effective.
        :type: bool
        """

        self._building_disabled = building_disabled

    @property
    def advanced_features(self):
        """
        Gets the advanced_features of this InlineResponse2006Effective.

        :return: The advanced_features of this InlineResponse2006Effective.
        :rtype: list[str]
        """
        return self._advanced_features

    @advanced_features.setter
    def advanced_features(self, advanced_features):
        """
        Sets the advanced_features of this InlineResponse2006Effective.

        :param advanced_features: The advanced_features of this InlineResponse2006Effective.
        :type: list[str]
        """

        self._advanced_features = advanced_features

    @property
    def scm_types(self):
        """
        Gets the scm_types of this InlineResponse2006Effective.

        :return: The scm_types of this InlineResponse2006Effective.
        :rtype: list[str]
        """
        return self._scm_types

    @scm_types.setter
    def scm_types(self, scm_types):
        """
        Sets the scm_types of this InlineResponse2006Effective.

        :param scm_types: The scm_types of this InlineResponse2006Effective.
        :type: list[str]
        """

        self._scm_types = scm_types

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2006Effective):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
