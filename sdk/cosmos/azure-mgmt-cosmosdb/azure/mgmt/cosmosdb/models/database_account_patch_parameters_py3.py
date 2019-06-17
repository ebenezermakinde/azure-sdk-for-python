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


class DatabaseAccountPatchParameters(Model):
    """Parameters for patching Azure Cosmos DB database account properties.

    :param tags:
    :type tags: dict[str, str]
    :param capabilities: List of Cosmos DB capabilities for the account
    :type capabilities: list[~azure.mgmt.cosmosdb.models.Capability]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'capabilities': {'key': 'properties.capabilities', 'type': '[Capability]'},
    }

    def __init__(self, *, tags=None, capabilities=None, **kwargs) -> None:
        super(DatabaseAccountPatchParameters, self).__init__(**kwargs)
        self.tags = tags
        self.capabilities = capabilities