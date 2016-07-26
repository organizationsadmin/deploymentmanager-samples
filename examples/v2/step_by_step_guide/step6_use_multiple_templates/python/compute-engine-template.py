# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates the Compute Engine."""


def GenerateConfig(unused_context):
  """Creates the Compute Engine with network and firewall."""

  resources = [{
      'name': 'vm-1',
      'type': 'vm-template.py'
  }, {
      'name': 'vm-2',
      'type': 'vm-template-2.py'
  }, {
      'name': 'network-1',
      'type': 'network-template.py'
  }, {
      'name': 'firewall-1',
      'type': 'firewall-template.py'
  }]
  return {'resources': resources}