import random
import sys
import uuid
import datetime
from marquez_client.models import (
    Namespace, Job, JobRun, Datasource, Dataset, RunState
)


class ModelGenerator:

    @staticmethod
    def new_owner_name():
        return "test_owner" + ModelGenerator._new_id()

    @staticmethod
    def new_namespace_name():
        return "test_namespace" + ModelGenerator._new_id()

    @staticmethod
    def new_job_name():
        return "test_job" + ModelGenerator._new_id()

    @staticmethod
    def new_location():
        return "https://github.com/repo/test/commit/" + ModelGenerator._new_id()

    @staticmethod
    def new_datasource_name():
        return "test_datasource" + ModelGenerator._new_id()

    @staticmethod
    def new_datasource_urn():
        return "urn:datasource:{}:{}".format(ModelGenerator._new_datasource_type(),
                                             ModelGenerator._new_db_name()) + ModelGenerator._new_id()

    @staticmethod
    def new_connection_url():
        return "jdbc:{}://localhost:5431/{}".format(ModelGenerator._new_datasource_type(),
                                                    ModelGenerator._new_db_name()) + ModelGenerator._new_id()

    @staticmethod
    def new_dataset_name():
        return "test_dataset" + ModelGenerator._new_id()

    @staticmethod
    def new_dataset_urns(limit):
        return [ModelGenerator.new_dataset_urn() for _ in range(limit)]

    @staticmethod
    def new_dataset_urn():
        return "urn:dataset:{}:public.room_bookings".format(ModelGenerator._new_db_name()) + ModelGenerator._new_id()

    @staticmethod
    def new_description():
        return "test_description" + ModelGenerator._new_id()

    @staticmethod
    def new_run_args():
        return "--email=wedata{}@wework.com".format(ModelGenerator._new_id())

    @staticmethod
    def new_run_id():
        return str(uuid.uuid4())

    @staticmethod
    def new_time_stamp():
        return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def new_run_state():
        return random.choice(list(RunState))

    @staticmethod
    def _new_id():
        return str(random.randint(1, sys.maxsize - 1))

    @staticmethod
    def _new_datasource_type():
        return random.choice(["redshift", "mysql", "postgresql"])

    @staticmethod
    def _new_db_name():
        return "test_db" + ModelGenerator._new_id()

    @staticmethod
    def new_namespace():
        return Namespace(ModelGenerator.new_namespace_name(), ModelGenerator.new_time_stamp(),
                         ModelGenerator.new_owner_name(), ModelGenerator.new_description())

    @staticmethod
    def new_job():
        time_stamp = ModelGenerator.new_time_stamp()
        return Job(ModelGenerator.new_job_name(), time_stamp, time_stamp, ModelGenerator.new_dataset_urns(3),
                   ModelGenerator.new_dataset_urns(4), ModelGenerator.new_location(), ModelGenerator.new_description())

    @staticmethod
    def new_jobrun():
        return JobRun(ModelGenerator.new_run_id(), ModelGenerator.new_time_stamp(), ModelGenerator.new_time_stamp(),
                      ModelGenerator.new_run_args(), ModelGenerator.new_run_state())

    @staticmethod
    def new_datasource():
        return Datasource(ModelGenerator.new_datasource_name(), ModelGenerator.new_time_stamp(),
                          ModelGenerator.new_datasource_urn(), ModelGenerator.new_connection_url())

    @staticmethod
    def new_dataset():
        return Dataset(ModelGenerator.new_dataset_name(), ModelGenerator.new_time_stamp(),
                       ModelGenerator.new_dataset_urn(), ModelGenerator.new_datasource_urn(),
                       ModelGenerator.new_description())

    @staticmethod
    def namespace_as_json(namespace):
        return {"name": namespace.name, "createdAt": namespace.created_at, "owner": namespace.owner_name,
                "description": namespace.description}

    @staticmethod
    def job_as_json(job):
        return {"name": job.name, "createdAt": job.created_at, "updatedAt": job.updated_at,
                "inputDatasetUrns": job.input_dataset_urns, "outputDatasetUrns": job.output_dataset_urns,
                "location": job.location, "description": job.description}

    @staticmethod
    def jobrun_as_json(jobrun):
        return {"runId": jobrun.run_id, "nominalStartTime": jobrun.nominal_start_time,
                "nominalEndTime": jobrun.nominal_end_time, "runArgs": jobrun.run_args, "runState": jobrun.run_state}

    @staticmethod
    def datasource_as_json(datasource):
        return {"name": datasource.name, "createdAt": datasource.created_at, "urn": datasource.urn,
                "connectionUrl": datasource.connection_url}

    @staticmethod
    def dataset_as_json(dataset):
        return {"name": dataset.name, "createdAt": dataset.created_at, "urn": dataset.urn,
                "datasourceUrn": dataset.datasource_urn, "description": dataset.description}
