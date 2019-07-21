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

from enum import Enum


class RunState(Enum):
    NEW = 'NEW'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    ABORTED = 'ABORTED'


class Namespace:
    def __init__(self, name, created_at, owner_name, description):
        self._name = name
        self._created_at = created_at
        self._owner_name = owner_name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def description(self):
        return self._description


class Job:
    def __init__(self, name, created_at, updated_at, input_dataset_urns,
                 output_dataset_urns, location, description):
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._input_dataset_urns = input_dataset_urns
        self._output_dataset_urns = output_dataset_urns
        self._location = location
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def input_dataset_urns(self):
        return self._input_dataset_urns

    @property
    def output_dataset_urns(self):
        return self._output_dataset_urns

    @property
    def location(self):
        return self._location

    @property
    def description(self):
        return self._description


class JobRun:
    def __init__(self, run_id, nominal_start_time,
                 nominal_end_time, run_args, run_state):
        self._run_id = run_id
        self._nominal_start_time = nominal_start_time
        self._nominal_end_time = nominal_end_time
        self._run_args = run_args
        self._run_state = run_state

    @property
    def run_id(self):
        return self._run_id

    @property
    def nominal_start_time(self):
        return self._nominal_start_time

    @property
    def nominal_end_time(self):
        return self._nominal_end_time

    @property
    def run_args(self):
        return self._run_args

    @property
    def run_state(self):
        return self._run_state


class Datasource:
    def __init__(self, name, created_at, urn, connection_url):
        self._name = name
        self._created_at = created_at
        self._urn = urn
        self._connection_url = connection_url

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def urn(self):
        return self._urn

    @property
    def connection_url(self):
        return self._connection_url


class Dataset:
    def __init__(self, name, created_at, urn, datasource_urn, description):
        self._name = name
        self._created_at = created_at
        self._urn = urn
        self._datasource_urn = datasource_urn
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def urn(self):
        return self._urn

    @property
    def datasource_urn(self):
        return self._datasource_urn

    @property
    def description(self):
        return self._description
