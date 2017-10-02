import cgi
import uuid

from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.topic import Topic


class AddTopicHandler(BaseHandler):
    def get(self):
        csrf_token = str(uuid.uuid4())
        memcache.add(csrf_token, True, time=600)

        params = {
            "csrf_token": csrf_token
        }
        return self.render_template("add_topic.html",
                                    params)

    def post(self):
        csrf_token = self.request.get('csrf-token')
        if not memcache.get(csrf_token):
            return self.write("CSRF NAPAD")

        title = cgi.escape(self.request.get('title'))
        text = cgi.escape(self.request.get('text'))

        email = users.get_current_user().email()

        topic = Topic(title=title, content=text,
              user_email=email)
        topic.put()
        return self.redirect('/')
