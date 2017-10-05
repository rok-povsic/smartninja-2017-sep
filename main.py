#!/usr/bin/env python
import webapp2

from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topic import AddTopicHandler, TopicDetailsHandler
from workers.send_mail_worker import SendMailWorker


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/add-topic', AddTopicHandler),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler),
    webapp2.Route('/task/email-topic-author', SendMailWorker),
], debug=True)
