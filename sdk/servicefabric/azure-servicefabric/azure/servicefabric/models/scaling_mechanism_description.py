# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ScalingMechanismDescription(Model):
    """Describes the mechanism for performing a scaling operation.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PartitionInstanceCountScaleMechanism,
    AddRemoveIncrementalNamedPartitionScalingMechanism

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'PartitionInstanceCount': 'PartitionInstanceCountScaleMechanism', 'AddRemoveIncrementalNamedPartition': 'AddRemoveIncrementalNamedPartitionScalingMechanism'}
    }

    def __init__(self, **kwargs):
        super(ScalingMechanismDescription, self).__init__(**kwargs)
        self.kind = None