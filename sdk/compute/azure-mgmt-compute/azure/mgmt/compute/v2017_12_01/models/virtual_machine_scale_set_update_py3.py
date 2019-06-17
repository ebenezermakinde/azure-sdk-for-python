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

from .update_resource_py3 import UpdateResource


class VirtualMachineScaleSetUpdate(UpdateResource):
    """Describes a Virtual Machine Scale Set.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The virtual machine scale set sku.
    :type sku: ~azure.mgmt.compute.v2017_12_01.models.Sku
    :param plan: The purchase plan when deploying a virtual machine scale set
     from VM Marketplace images.
    :type plan: ~azure.mgmt.compute.v2017_12_01.models.Plan
    :param upgrade_policy: The upgrade policy.
    :type upgrade_policy: ~azure.mgmt.compute.v2017_12_01.models.UpgradePolicy
    :param virtual_machine_profile: The virtual machine profile.
    :type virtual_machine_profile:
     ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetUpdateVMProfile
    :param overprovision: Specifies whether the Virtual Machine Scale Set
     should be overprovisioned.
    :type overprovision: bool
    :param single_placement_group: When true this limits the scale set to a
     single placement group, of max size 100 virtual machines.
    :type single_placement_group: bool
    :param identity: The identity of the virtual machine scale set, if
     configured.
    :type identity:
     ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetIdentity
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'upgrade_policy': {'key': 'properties.upgradePolicy', 'type': 'UpgradePolicy'},
        'virtual_machine_profile': {'key': 'properties.virtualMachineProfile', 'type': 'VirtualMachineScaleSetUpdateVMProfile'},
        'overprovision': {'key': 'properties.overprovision', 'type': 'bool'},
        'single_placement_group': {'key': 'properties.singlePlacementGroup', 'type': 'bool'},
        'identity': {'key': 'identity', 'type': 'VirtualMachineScaleSetIdentity'},
    }

    def __init__(self, *, tags=None, sku=None, plan=None, upgrade_policy=None, virtual_machine_profile=None, overprovision: bool=None, single_placement_group: bool=None, identity=None, **kwargs) -> None:
        super(VirtualMachineScaleSetUpdate, self).__init__(tags=tags, **kwargs)
        self.sku = sku
        self.plan = plan
        self.upgrade_policy = upgrade_policy
        self.virtual_machine_profile = virtual_machine_profile
        self.overprovision = overprovision
        self.single_placement_group = single_placement_group
        self.identity = identity