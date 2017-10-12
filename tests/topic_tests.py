import os
import unittest
import webapp2
import webtest

from google.appengine.ext import testbed
from google.appengine.api import memcache

from handlers.topic import AddTopicHandler
from models.topic import Topic


class TopicTests(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication(
            [
                webapp2.Route('/topic/add', AddTopicHandler),
            ])

        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        """ Uncomment the stubs that you need to run tests. """
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # self.testbed.init_mail_stub()
        # self.testbed.init_taskqueue_stub()
        self.testbed.init_user_stub()
        # ...

        """ Uncomment if you need user (Google Login) and if this user needs to be admin. """
        os.environ['USER_EMAIL'] = 'some.user@example.com'
        # os.environ['USER_IS_ADMIN'] = '1'

    def tearDown(self):
        self.testbed.deactivate()

    def test_add_topic_handler(self):
        memcache.add(key='abc123', value=True)

        params = {
            'title': 'Nova tema',
            'text': 'Neka vsebina teme.',
            'csrf-token': 'abc123'
        }
        response = self.testapp.post('/topic/add',
                                     params)
        self.assertEquals(
            response.status_int, 302)

        topic = Topic.query().get()
        self.assertEqual('Nova tema', topic.title)