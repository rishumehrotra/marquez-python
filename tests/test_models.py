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
from marquez_client.models import (
    Namespace, Job, JobRun, Datasource, Dataset
)
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


def test_namespace_factory():
    namespace_expected = ModelGenerator.new_namespace()
    namespace_json = ModelGenerator.namespace_as_json(namespace_expected)

    namespace_actual = Namespace.from_response(namespace_json)

    assert namespace_actual.name == namespace_expected.name
    assert namespace_actual.created_at == namespace_expected.created_at
    assert namespace_actual.owner_name == namespace_expected.owner_name
    assert namespace_actual.description == namespace_expected.description


def test_initialize_job():
    name = ModelGenerator.new_job_name()
    created_at = ModelGenerator.new_time_stamp()
    updated_at = created_at
    input_dataset_urns = ModelGenerator.new_dataset_urns(3)
    output_dataset_urns = ModelGenerator.new_dataset_urns(4)
    location = ModelGenerator.new_location()
    description = ModelGenerator.new_description()

    job = Job(name, created_at, updated_at, input_dataset_urns, output_dataset_urns, location, description)

    assert name == job.name
    assert created_at == job.created_at
    assert updated_at == job.updated_at
    assert input_dataset_urns == job.input_dataset_urns
    assert output_dataset_urns == job.output_dataset_urns
    assert location == job.location
    assert description == job.description


def test_job_factory():
    job_expected = ModelGenerator.new_job()
    job_json = ModelGenerator.job_as_json(job_expected)

    job_actual = Job.from_response(job_json)

    assert job_expected.name == job_actual.name
    assert job_expected.created_at == job_actual.created_at
    assert job_expected.updated_at == job_actual.updated_at
    assert job_expected.input_dataset_urns == job_actual.input_dataset_urns
    assert job_expected.output_dataset_urns == job_actual.output_dataset_urns
    assert job_expected.location == job_actual.location
    assert job_expected.description == job_actual.description


def test_initialize_jobrun():
    run_id = ModelGenerator.new_run_id()
    nominal_start_time = ModelGenerator.new_time_stamp()
    nominal_end_time = ModelGenerator.new_time_stamp()
    run_args = ModelGenerator.new_run_args()
    run_state = ModelGenerator.new_run_state()

    job_run = JobRun(run_id, nominal_start_time, nominal_end_time, run_args, run_state)

    assert run_id == job_run.run_id
    assert nominal_start_time == job_run.nominal_start_time
    assert nominal_end_time == job_run.nominal_end_time
    assert run_args == job_run.run_args
    assert run_state == job_run.run_state


def test_jobrun_factory():
    jobrun_expected = ModelGenerator.new_jobrun()
    jobrun_json = ModelGenerator.jobrun_as_json(jobrun_expected)

    jobrun_actual = JobRun.from_response(jobrun_json)

    assert jobrun_expected.run_id == jobrun_actual.run_id
    assert jobrun_expected.nominal_start_time == jobrun_actual.nominal_start_time
    assert jobrun_expected.nominal_end_time == jobrun_actual.nominal_end_time
    assert jobrun_expected.run_args == jobrun_actual.run_args
    assert jobrun_expected.run_state == jobrun_actual.run_state


def test_initialize_datasource():
    name = ModelGenerator.new_datasource_name()
    created_at = ModelGenerator.new_time_stamp()
    urn = ModelGenerator.new_datasource_urn()
    connection_url = ModelGenerator.new_connection_url()

    datasource = Datasource(name, created_at, urn, connection_url)

    assert name == datasource.name
    assert created_at == datasource.created_at
    assert urn == datasource.urn
    assert connection_url == datasource.connection_url


def test_datasource_factory():
    datasource_expected = ModelGenerator.new_datasource()
    datasource_json = ModelGenerator.datasource_as_json(datasource_expected)

    datasource_actual = Datasource.from_response(datasource_json)

    assert datasource_expected.name == datasource_actual.name
    assert datasource_expected.created_at == datasource_actual.created_at
    assert datasource_expected.urn == datasource_actual.urn
    assert datasource_expected.connection_url == datasource_actual.connection_url


def test_initialize_dataset():
    name = ModelGenerator.new_dataset_name()
    created_at = ModelGenerator.new_time_stamp()
    urn = ModelGenerator.new_dataset_urn()
    datasource_urn = ModelGenerator.new_datasource_urn()
    description = ModelGenerator.new_description()

    dataset = Dataset(name, created_at, urn, datasource_urn, description)

    assert name == dataset.name
    assert created_at == dataset.created_at
    assert urn == dataset.urn
    assert datasource_urn == dataset.datasource_urn
    assert description == dataset.description


def test_dataset_factory():
    dataset_expected = ModelGenerator.new_dataset()
    dataset_json = ModelGenerator.dataset_as_json(dataset_expected)

    dataset_actual = Dataset.from_response(dataset_json)

    assert dataset_expected.name == dataset_actual.name
    assert dataset_expected.created_at == dataset_actual.created_at
    assert dataset_expected.urn == dataset_actual.urn
    assert dataset_expected.datasource_urn == dataset_actual.datasource_urn
    assert dataset_expected.description == dataset_actual.description