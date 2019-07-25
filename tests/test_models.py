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

import pytest
from marquez_client.models import Namespace
from .model_generator import ModelGenerator


def test_initialize_namespace():
    name = ModelGenerator.new_namespace_name()
    created_at = ModelGenerator.new_time_stamp()
    owner_name = ModelGenerator.new_owner_name()
    description = ModelGenerator.new_description()

    namespace = Namespace(name, created_at, owner_name, description)

    assert name == namespace.name
    assert created_at == namespace.created_at
    assert owner_name == namespace.owner_name
    assert description == namespace.description
