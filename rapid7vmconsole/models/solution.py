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

from rapid7vmconsole.models.additional_information import AdditionalInformation  # noqa: F401,E501
from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.steps import Steps  # noqa: F401,E501
from rapid7vmconsole.models.summary import Summary  # noqa: F401,E501


class Solution(object):
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
        'additional_information': 'AdditionalInformation',
        'applies_to': 'str',
        'estimate': 'str',
        'id': 'str',
        'links': 'list[Link]',
        'steps': 'Steps',
        'summary': 'Summary',
        'type': 'str'
    }

    attribute_map = {
        'additional_information': 'additionalInformation',
        'applies_to': 'appliesTo',
        'estimate': 'estimate',
        'id': 'id',
        'links': 'links',
        'steps': 'steps',
        'summary': 'summary',
        'type': 'type'
    }

    def __init__(self, additional_information=None, applies_to=None, estimate=None, id=None, links=None, steps=None, summary=None, type=None):  # noqa: E501
        """Solution - a model defined in Swagger"""  # noqa: E501

        self._additional_information = None
        self._applies_to = None
        self._estimate = None
        self._id = None
        self._links = None
        self._steps = None
        self._summary = None
        self._type = None
        self.discriminator = None

        if additional_information is not None:
            self.additional_information = additional_information
        if applies_to is not None:
            self.applies_to = applies_to
        if estimate is not None:
            self.estimate = estimate
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if steps is not None:
            self.steps = steps
        if summary is not None:
            self.summary = summary
        if type is not None:
            self.type = type

    @property
    def additional_information(self):
        """Gets the additional_information of this Solution.  # noqa: E501

        Additional information or resources that can assist in applying the remediation.  # noqa: E501

        :return: The additional_information of this Solution.  # noqa: E501
        :rtype: AdditionalInformation
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this Solution.

        Additional information or resources that can assist in applying the remediation.  # noqa: E501

        :param additional_information: The additional_information of this Solution.  # noqa: E501
        :type: AdditionalInformation
        """

        self._additional_information = additional_information

    @property
    def applies_to(self):
        """Gets the applies_to of this Solution.  # noqa: E501

        The systems or software the solution applies to.  # noqa: E501

        :return: The applies_to of this Solution.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this Solution.

        The systems or software the solution applies to.  # noqa: E501

        :param applies_to: The applies_to of this Solution.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def estimate(self):
        """Gets the estimate of this Solution.  # noqa: E501

        The estimated duration to apply the solution, in ISO 8601 format. For example: `\"PT5M\"`.  # noqa: E501

        :return: The estimate of this Solution.  # noqa: E501
        :rtype: str
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this Solution.

        The estimated duration to apply the solution, in ISO 8601 format. For example: `\"PT5M\"`.  # noqa: E501

        :param estimate: The estimate of this Solution.  # noqa: E501
        :type: str
        """

        self._estimate = estimate

    @property
    def id(self):
        """Gets the id of this Solution.  # noqa: E501

        The identifier of the solution.  # noqa: E501

        :return: The id of this Solution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Solution.

        The identifier of the solution.  # noqa: E501

        :param id: The id of this Solution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this Solution.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Solution.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Solution.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Solution.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def steps(self):
        """Gets the steps of this Solution.  # noqa: E501

        The steps required to remediate the vulnerability.  # noqa: E501

        :return: The steps of this Solution.  # noqa: E501
        :rtype: Steps
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Solution.

        The steps required to remediate the vulnerability.  # noqa: E501

        :param steps: The steps of this Solution.  # noqa: E501
        :type: Steps
        """

        self._steps = steps

    @property
    def summary(self):
        """Gets the summary of this Solution.  # noqa: E501

        The summary of the solution.  # noqa: E501

        :return: The summary of this Solution.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Solution.

        The summary of the solution.  # noqa: E501

        :param summary: The summary of this Solution.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def type(self):
        """Gets the type of this Solution.  # noqa: E501

        The type of the solution. One of: `\"Configuration\"`, `\"Rollup patch\"`, `\"Patch\"`  # noqa: E501

        :return: The type of this Solution.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Solution.

        The type of the solution. One of: `\"Configuration\"`, `\"Rollup patch\"`, `\"Patch\"`  # noqa: E501

        :param type: The type of this Solution.  # noqa: E501
        :type: str
        """
        allowed_values = ["configuration", "rollup-patch", "patch", "unknown"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(Solution, dict):
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
        if not isinstance(other, Solution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
