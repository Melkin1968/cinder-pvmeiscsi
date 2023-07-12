#! /usr/bin/env python3

# Copyright 2021 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from ops_openstack.plugins.classes import CinderStoragePluginCharm
from ops_openstack.core import charm_class, get_charm_class_for_release
from ops.main import main


class CinderPVMEISCSICharm(CinderStoragePluginCharm):

    PACKAGES = ['cinder-common']
    # Overriden from the parent. May be set depending on the charm's properties
    stateless = True
    active_active = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cinder_configuration(self, config):
        # Return the configuration to be set by the principal.
        volume_driver = 'cinder.volume.drivers.dell_emc.powervault.iscsi.PVMEISCSIDriver'
        options = [
            ('volume_driver', volume_driver),
            ('volume_backend_name', 'cinder-pvme'),
            ('pvme_pool_name', config['pvme_pool_name']),
            ('san_ip', config['san_ip']),
            ('san_login', config['san_login']),
            ('san_password', config['san_password']),
            ('pvme_iscsi_ips', config['pvme_iscsi_ips']),
            ('driver_use_ssl', config['driver_use_ssl']),
        ]
        


        if config.get('driver_use_ssl'):
            options.extend([
                ('driver_ssl_cert_verify', config['driver_ssl_cert_verify']),
#               ('driver_ssl_cert_path', config['driver_ssl_cert_path'])
            ])

        return options


if __name__ == '__main__':
    main(CinderPVMEISCSICharm)
