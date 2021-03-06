# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.policy import Policy  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_database import ScanTemplateDatabase  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_discovery import ScanTemplateDiscovery  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_vulnerability_checks import ScanTemplateVulnerabilityChecks  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_web_spider import ScanTemplateWebSpider  # noqa: F401,E501
from rapid7vmconsole.models.telnet import Telnet  # noqa: F401,E501


class ScanTemplate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'checks': 'ScanTemplateVulnerabilityChecks',
        'database': 'ScanTemplateDatabase',
        'description': 'str',
        'discovery': 'ScanTemplateDiscovery',
        'discovery_only': 'bool',
        'enable_windows_services': 'bool',
        'enhanced_logging': 'bool',
        'id': 'str',
        'links': 'list[Link]',
        'max_parallel_assets': 'int',
        'max_scan_processes': 'int',
        'name': 'str',
        'policy': 'Policy',
        'policy_enabled': 'bool',
        'telnet': 'Telnet',
        'vulnerability_enabled': 'bool',
        'web': 'ScanTemplateWebSpider',
        'web_enabled': 'bool'
    }

    attribute_map = {
        'checks': 'checks',
        'database': 'database',
        'description': 'description',
        'discovery': 'discovery',
        'discovery_only': 'discoveryOnly',
        'enable_windows_services': 'enableWindowsServices',
        'enhanced_logging': 'enhancedLogging',
        'id': 'id',
        'links': 'links',
        'max_parallel_assets': 'maxParallelAssets',
        'max_scan_processes': 'maxScanProcesses',
        'name': 'name',
        'policy': 'policy',
        'policy_enabled': 'policyEnabled',
        'telnet': 'telnet',
        'vulnerability_enabled': 'vulnerabilityEnabled',
        'web': 'web',
        'web_enabled': 'webEnabled'
    }

    def __init__(self, checks=None, database=None, description=None, discovery=None, discovery_only=None, enable_windows_services=None, enhanced_logging=None, id=None, links=None, max_parallel_assets=None, max_scan_processes=None, name=None, policy=None, policy_enabled=None, telnet=None, vulnerability_enabled=None, web=None, web_enabled=None):  # noqa: E501
        """ScanTemplate - a model defined in Swagger"""  # noqa: E501

        self._checks = None
        self._database = None
        self._description = None
        self._discovery = None
        self._discovery_only = None
        self._enable_windows_services = None
        self._enhanced_logging = None
        self._id = None
        self._links = None
        self._max_parallel_assets = None
        self._max_scan_processes = None
        self._name = None
        self._policy = None
        self._policy_enabled = None
        self._telnet = None
        self._vulnerability_enabled = None
        self._web = None
        self._web_enabled = None
        self.discriminator = None

        if checks is not None:
            self.checks = checks
        if database is not None:
            self.database = database
        if description is not None:
            self.description = description
        if discovery is not None:
            self.discovery = discovery
        if discovery_only is not None:
            self.discovery_only = discovery_only
        if enable_windows_services is not None:
            self.enable_windows_services = enable_windows_services
        if enhanced_logging is not None:
            self.enhanced_logging = enhanced_logging
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if max_parallel_assets is not None:
            self.max_parallel_assets = max_parallel_assets
        if max_scan_processes is not None:
            self.max_scan_processes = max_scan_processes
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if policy_enabled is not None:
            self.policy_enabled = policy_enabled
        if telnet is not None:
            self.telnet = telnet
        if vulnerability_enabled is not None:
            self.vulnerability_enabled = vulnerability_enabled
        if web is not None:
            self.web = web
        if web_enabled is not None:
            self.web_enabled = web_enabled

    @property
    def checks(self):
        """Gets the checks of this ScanTemplate.  # noqa: E501

        Settings for which vulnerability checks to run during a scan. <br/>  The rules for inclusion of checks is as follows:  <ul>  <li>Enabled checks by category and by check type are included</li>  <li>Disabled checks in by category and by check type are removed</li>  <li>Enabled checks in by individual check are added (even if they are disabled in by category or check type)</li>  <li>Disabled checks in by individual check are removed</li>  <li>If unsafe is disabled, unsafe checks are removed</li>  <li>If potential is disabled, potential checks are removed</li>  <ul>  # noqa: E501

        :return: The checks of this ScanTemplate.  # noqa: E501
        :rtype: ScanTemplateVulnerabilityChecks
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this ScanTemplate.

        Settings for which vulnerability checks to run during a scan. <br/>  The rules for inclusion of checks is as follows:  <ul>  <li>Enabled checks by category and by check type are included</li>  <li>Disabled checks in by category and by check type are removed</li>  <li>Enabled checks in by individual check are added (even if they are disabled in by category or check type)</li>  <li>Disabled checks in by individual check are removed</li>  <li>If unsafe is disabled, unsafe checks are removed</li>  <li>If potential is disabled, potential checks are removed</li>  <ul>  # noqa: E501

        :param checks: The checks of this ScanTemplate.  # noqa: E501
        :type: ScanTemplateVulnerabilityChecks
        """

        self._checks = checks

    @property
    def database(self):
        """Gets the database of this ScanTemplate.  # noqa: E501

        Settings for discovery databases.  # noqa: E501

        :return: The database of this ScanTemplate.  # noqa: E501
        :rtype: ScanTemplateDatabase
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ScanTemplate.

        Settings for discovery databases.  # noqa: E501

        :param database: The database of this ScanTemplate.  # noqa: E501
        :type: ScanTemplateDatabase
        """

        self._database = database

    @property
    def description(self):
        """Gets the description of this ScanTemplate.  # noqa: E501

        A verbose description of the scan template..  # noqa: E501

        :return: The description of this ScanTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScanTemplate.

        A verbose description of the scan template..  # noqa: E501

        :param description: The description of this ScanTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discovery(self):
        """Gets the discovery of this ScanTemplate.  # noqa: E501

        Discovery settings used during a scan.  # noqa: E501

        :return: The discovery of this ScanTemplate.  # noqa: E501
        :rtype: ScanTemplateDiscovery
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this ScanTemplate.

        Discovery settings used during a scan.  # noqa: E501

        :param discovery: The discovery of this ScanTemplate.  # noqa: E501
        :type: ScanTemplateDiscovery
        """

        self._discovery = discovery

    @property
    def discovery_only(self):
        """Gets the discovery_only of this ScanTemplate.  # noqa: E501

        Whether only discovery is performed during a scan.  # noqa: E501

        :return: The discovery_only of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._discovery_only

    @discovery_only.setter
    def discovery_only(self, discovery_only):
        """Sets the discovery_only of this ScanTemplate.

        Whether only discovery is performed during a scan.  # noqa: E501

        :param discovery_only: The discovery_only of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._discovery_only = discovery_only

    @property
    def enable_windows_services(self):
        """Gets the enable_windows_services of this ScanTemplate.  # noqa: E501

        Whether Windows services are enabled during a scan. Windows services will be temporarily reconfigured when this option is selected. Original settings will be restored after the scan completes, unless it is interrupted.  # noqa: E501

        :return: The enable_windows_services of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._enable_windows_services

    @enable_windows_services.setter
    def enable_windows_services(self, enable_windows_services):
        """Sets the enable_windows_services of this ScanTemplate.

        Whether Windows services are enabled during a scan. Windows services will be temporarily reconfigured when this option is selected. Original settings will be restored after the scan completes, unless it is interrupted.  # noqa: E501

        :param enable_windows_services: The enable_windows_services of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._enable_windows_services = enable_windows_services

    @property
    def enhanced_logging(self):
        """Gets the enhanced_logging of this ScanTemplate.  # noqa: E501

        Whether enhanced logging is gathered during scanning. Collection of enhanced logs may greatly increase the disk space used by a scan.  # noqa: E501

        :return: The enhanced_logging of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._enhanced_logging

    @enhanced_logging.setter
    def enhanced_logging(self, enhanced_logging):
        """Sets the enhanced_logging of this ScanTemplate.

        Whether enhanced logging is gathered during scanning. Collection of enhanced logs may greatly increase the disk space used by a scan.  # noqa: E501

        :param enhanced_logging: The enhanced_logging of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._enhanced_logging = enhanced_logging

    @property
    def id(self):
        """Gets the id of this ScanTemplate.  # noqa: E501

        The identifier of the scan template  # noqa: E501

        :return: The id of this ScanTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScanTemplate.

        The identifier of the scan template  # noqa: E501

        :param id: The id of this ScanTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this ScanTemplate.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this ScanTemplate.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ScanTemplate.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this ScanTemplate.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def max_parallel_assets(self):
        """Gets the max_parallel_assets of this ScanTemplate.  # noqa: E501

        The maximum number of assets scanned simultaneously per scan engine during a scan.  # noqa: E501

        :return: The max_parallel_assets of this ScanTemplate.  # noqa: E501
        :rtype: int
        """
        return self._max_parallel_assets

    @max_parallel_assets.setter
    def max_parallel_assets(self, max_parallel_assets):
        """Sets the max_parallel_assets of this ScanTemplate.

        The maximum number of assets scanned simultaneously per scan engine during a scan.  # noqa: E501

        :param max_parallel_assets: The max_parallel_assets of this ScanTemplate.  # noqa: E501
        :type: int
        """

        self._max_parallel_assets = max_parallel_assets

    @property
    def max_scan_processes(self):
        """Gets the max_scan_processes of this ScanTemplate.  # noqa: E501

        The maximum number of scan processes simultaneously allowed against each asset during a scan.  # noqa: E501

        :return: The max_scan_processes of this ScanTemplate.  # noqa: E501
        :rtype: int
        """
        return self._max_scan_processes

    @max_scan_processes.setter
    def max_scan_processes(self, max_scan_processes):
        """Sets the max_scan_processes of this ScanTemplate.

        The maximum number of scan processes simultaneously allowed against each asset during a scan.  # noqa: E501

        :param max_scan_processes: The max_scan_processes of this ScanTemplate.  # noqa: E501
        :type: int
        """

        self._max_scan_processes = max_scan_processes

    @property
    def name(self):
        """Gets the name of this ScanTemplate.  # noqa: E501

        A concise name for the scan template.  # noqa: E501

        :return: The name of this ScanTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScanTemplate.

        A concise name for the scan template.  # noqa: E501

        :param name: The name of this ScanTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this ScanTemplate.  # noqa: E501

        Policy configuration settings used during a scan.  # noqa: E501

        :return: The policy of this ScanTemplate.  # noqa: E501
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ScanTemplate.

        Policy configuration settings used during a scan.  # noqa: E501

        :param policy: The policy of this ScanTemplate.  # noqa: E501
        :type: Policy
        """

        self._policy = policy

    @property
    def policy_enabled(self):
        """Gets the policy_enabled of this ScanTemplate.  # noqa: E501

        Whether policy assessment is performed during a scan.  # noqa: E501

        :return: The policy_enabled of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._policy_enabled

    @policy_enabled.setter
    def policy_enabled(self, policy_enabled):
        """Sets the policy_enabled of this ScanTemplate.

        Whether policy assessment is performed during a scan.  # noqa: E501

        :param policy_enabled: The policy_enabled of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._policy_enabled = policy_enabled

    @property
    def telnet(self):
        """Gets the telnet of this ScanTemplate.  # noqa: E501

        Settings for interacting with the Telnet protocol.  # noqa: E501

        :return: The telnet of this ScanTemplate.  # noqa: E501
        :rtype: Telnet
        """
        return self._telnet

    @telnet.setter
    def telnet(self, telnet):
        """Sets the telnet of this ScanTemplate.

        Settings for interacting with the Telnet protocol.  # noqa: E501

        :param telnet: The telnet of this ScanTemplate.  # noqa: E501
        :type: Telnet
        """

        self._telnet = telnet

    @property
    def vulnerability_enabled(self):
        """Gets the vulnerability_enabled of this ScanTemplate.  # noqa: E501

        Whether vulnerability assessment is performed during a scan.  # noqa: E501

        :return: The vulnerability_enabled of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._vulnerability_enabled

    @vulnerability_enabled.setter
    def vulnerability_enabled(self, vulnerability_enabled):
        """Sets the vulnerability_enabled of this ScanTemplate.

        Whether vulnerability assessment is performed during a scan.  # noqa: E501

        :param vulnerability_enabled: The vulnerability_enabled of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._vulnerability_enabled = vulnerability_enabled

    @property
    def web(self):
        """Gets the web of this ScanTemplate.  # noqa: E501

        Web spider settings used during a scan.  # noqa: E501

        :return: The web of this ScanTemplate.  # noqa: E501
        :rtype: ScanTemplateWebSpider
        """
        return self._web

    @web.setter
    def web(self, web):
        """Sets the web of this ScanTemplate.

        Web spider settings used during a scan.  # noqa: E501

        :param web: The web of this ScanTemplate.  # noqa: E501
        :type: ScanTemplateWebSpider
        """

        self._web = web

    @property
    def web_enabled(self):
        """Gets the web_enabled of this ScanTemplate.  # noqa: E501

        Whether web spidering and assessment are performed during a scan.  # noqa: E501

        :return: The web_enabled of this ScanTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._web_enabled

    @web_enabled.setter
    def web_enabled(self, web_enabled):
        """Sets the web_enabled of this ScanTemplate.

        Whether web spidering and assessment are performed during a scan.  # noqa: E501

        :param web_enabled: The web_enabled of this ScanTemplate.  # noqa: E501
        :type: bool
        """

        self._web_enabled = web_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ScanTemplate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScanTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
