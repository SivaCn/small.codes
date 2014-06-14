#!/usr/bin/python


import pika
import time
import urllib2
import httplib
import xmlrpclib
import pymongo
from bson.objectid import ObjectId
from scheduler_authentication import BasicAuthTransport


DOC_WIDTH = 120


class RemoteMachine(object):
    def __xmlrpc(self, **kwargs):
        """Connects to the Remote machine."""
        ## Validate arguments.
        must_arg_lst = ['username', 'password', 'hostname', 'port']
        for args in must_arg_lst:
            if args not in kwargs:
                raise Exception("Expecting mandatory keyword argument {0}, Got None".format(args))

        username = kwargs.get('username')
        password = kwargs.get('password')
        hostname = kwargs.get('hostname')
        port = kwargs.get('port')

        path = '/cms/Sentinel/SentinelEngine'

        is_secured_site = 'https' if kwargs.get('is_secured', False) else 'http'

        auth_token = BasicAuthTransport(username, password, https=is_secured_site)

        url = """{0}://{1}:{2}{3}""".format(is_secured_site, hostname, port, path)

        server = xmlrpclib.Server(url, auth_token)

        return server

    def authenticate_user(self, **kwargs):
        """."""
        server_obj = self.__xmlrpc(**kwargs)
        if server_obj:
            return True
        return False

    def execute_remote_method(self, **kwargs):
        """."""
        server_obj = self.__xmlrpc()
        if server_obj:
            server_obj.runSentinelRule()
            ##server_obj.runSentinelRule(event, business_process, rule_type, create_event, check_duplicate_event)
        return False

class Http(object):
    def get_status_code(self, **kwargs):
        """."""
        hostname = kwargs.get('hostname', '')
        port = kwargs.get('port', '')
        path = kwargs.get('path', '')

        if not hostname:
            raise Exception("Expecting must argument hostname, Got None")

        try:
            conn = httplib.HTTPConnection("{0}{1}".format(hostname, ':{0}'.format(port) if port else ''))
            conn.request("HEAD", path)
            return conn.getresponse().status
        except StandardError:
            return None

class ZopeInstance(RemoteMachine):
    def user_authentication(self, **kwargs):
        """."""
        return self.authenticate_user(**kwargs)

    def run(self, **kwargs):
        """."""
        return self.execute_remote_method(**kwargs)


class MongoDB(Http):
    """Test Against MongoDB."""
    def is_running(self, _report, **kwargs):
        """Test Weather the MongoDB is running as a Service or not.."""
        hostname = kwargs.get('host', '')
        port = kwargs.get('port', '')

        if port:
            port = port + 1000

        print >> _report, "START: MongoDB Test on Service"

        status = self.get_status_code(hostname=hostname, port=port)

        print >> _report, "Hostname: {0}, Port:{1}".format(hostname, port)
        print >> _report, "Http Status Code: {0}".format(status)
        print >> _report, "RESULT: {0}".format('SUCCESS' if status == 200 else 'FAILURE')
        print >> _report, "END: MongoDB Test on Service"
        print >> _report, "-" * DOC_WIDTH

        if status == 200:
            return True
        return False

    def test_insert(self, _report, **kwargs):
        """Test MongoDB by inserting some data into it."""
        hostname = kwargs.get('host', '')
        port = kwargs.get('port', '')

        print >> _report, "START: MongoDB Test on Dump"
        print >> _report, "Hostname: {0}, Port:{1}".format(hostname, port)

        try:
            client = pymongo.Connection(hostname, port)
            db = client.TestService
            collection_name = "TestService"

            print >> _report, "Database Name: TestServices"
            print >> _report, "Collection Name: {0}".format(collection_name)

            if not collection_name in db.collection_names():
                collection = db.create_collection(collection_name)
            else:
                collection = db[collection_name]

            _data = {'TEST': 'TEST'}
            res = collection.save(_data)

            print >> _report, "Data Inserted: {0}".format(_data)
            print >> _report, "RESULT: {0}".format('SUCCESS' if res else 'FAILURE')

        except:
            print >> _report, "Unable to Insert data into MongoDB"
            print >> _report, "RESULT: FAILURE"

        finally:
            print >> _report, "END: MongoDB Test on Dump"
            print >> _report, "-" * DOC_WIDTH

class RabbitMQ(Http):
    def is_running(self, _report, **kwargs):
        """Test Weather the RabbitMQ is running as a Service or not.."""
        hostname = kwargs.get('host', '')
        port = kwargs.get('port', '')
        port = port + 10000

        print >> _report, "START: RabbitMQ Test on Service"

        status = self.get_status_code(hostname=hostname, port=port)

        print >> _report, "Hostname: {0}, Port:{1}".format(hostname, port)
        print >> _report, "Http Status Code: {0}".format(status)
        print >> _report, "RESULT: {0}".format('SUCCESS' if status == 200 else 'FAILURE')
        print >> _report, "END: RabbitMQ Test on Service"
        print >> _report, "-" * DOC_WIDTH

        if status == 200:
            return True
        return False

    def test_enque(self, _report, **kwargs):
        """Try Publishing a sample message to RabbitMQ."""
        hostname = kwargs.get('host', '')
        port = kwargs.get('port', '')

        try:
            print >> _report, "START: RabbitMQ Test on Enqueing RabbitMQ"
            parameters = pika.URLParameters("amqp://guest:guest@{0}:{1}/%2F".format(hostname, port))
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            channel.basic_publish('test_exchange',
                                  'test_routing_key',
                                  'message body value',
                                  pika.BasicProperties(content_type='text/plain',
                                                       delivery_mode=1))

            connection.close()
            print >> _report, "Successfully Published Message to RabbitMQ"
            print >> _report, "RESULT: SUCCESS"
            return True

        except:
            print >> _report, "Unable to publish message to RabbitMQ"
            print >> _report, "RESULT: FAILURE"
            return False
        finally:
            print >> _report, "END: RabbitMQ Test on Enqueing RabbitMQ"
            print >> _report, "-" * DOC_WIDTH

class Report(object):
    """."""
    def __init__(self):
        self.msg = []

    def write(self, _msg):
        """."""
        if not _msg.strip():
            return

        if _msg.startswith('--') or _msg.startswith('=='):
            self.msg.append(_msg + '\n')
        else:
            _template = """{0}:  {1}\n""".format(time.ctime(time.time()), _msg)
            self.msg.append(_template)

class TestRun(object):
    """."""
    ## Config Reads.
    zope_url_or_ip = 'localhost'
    zope_port = 4547
    is_https = False
    mongo_host = 'localhost'
    mongo_port = 27017
    rabbitmq_host = 'localhost'
    rabbitmq_port = 5672

    ## Objects.
    mongo = MongoDB()
    mq = RabbitMQ()

    @classmethod
    def run(cls, _report):
        """."""
        print >> _report, "=" * DOC_WIDTH
        print >> _report, "--- TESTING ---"
        print >> _report, "-" * DOC_WIDTH

        cls.mongo.is_running(_report, host=cls.mongo_host, port=cls.mongo_port)
        cls.mongo.test_insert(_report, host=cls.mongo_host, port=cls.mongo_port)

        cls.mq.is_running(_report, host=cls.rabbitmq_host, port=cls.rabbitmq_port)
        cls.mq.test_enque(_report, host=cls.rabbitmq_host, port=cls.rabbitmq_port)

        return _report

if __name__ == '__main__':
    _report = Report()
    obj = TestRun()
    _report = obj.run(_report)

    print ''.join(_report.msg)
