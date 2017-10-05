import cgi
import uuid

from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment


def make_csrf_token():
    csrf_token = str(uuid.uuid4())
    memcache.add(csrf_token, True, time=600)
    return csrf_token


class AddTopicHandler(BaseHandler):
    def get(self):
        params = {
            "csrf_token": make_csrf_token()
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


class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == int(topic_id)).fetch()

        params = {
            "csrf_token": make_csrf_token(),
            "topic": topic,
            "comments": comments,
        }
        return self.render_template("topic_details.html",
                                    params)

    def post(self, topic_id):
        csrf_token = self.request.get('csrf-token')
        if not memcache.get(csrf_token):
            return self.write("CSRF NAPAD")

        text = cgi.escape(self.request.get('text'))

        Comment.create_comment(topic_id, text)

        return self.redirect('/')
