#!/usr/bin/env python
import webapp2

from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topic import AddTopicHandler, TopicDetailsHandler, DeleteTopicHandler
from workers.send_mail_worker import SendMailWorker
from crons.delete_topics_cron import DeleteTopicsCron
from handlers.stock import StockHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/set-cookie', CookieHandler),

    webapp2.Route('/add-topic', AddTopicHandler),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler),
    webapp2.Route('/topic-delete/<topic_id:\d+>', DeleteTopicHandler),
    webapp2.Route('/stock', StockHandler),

    webapp2.Route('/task/email-topic-author', SendMailWorker),

    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
], debug=True)
