import random
import sys
import uuid
import datetime


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
    def _new_id():
        return str(random.randint(1, sys.maxsize - 1))

    @staticmethod
    def _new_datasource_type():
        return random.choice(["redshift", "mysql", "postgresql"])

    @staticmethod
    def _new_db_name():
        return "test_db" + ModelGenerator._new_id()
