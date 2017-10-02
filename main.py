#!/usr/bin/env python
import webapp2

from handlers.main import MainHandler
from handlers.cookie import CookieHandler
from handlers.topic import AddTopicHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/add-topic', AddTopicHandler),
], debug=True)
