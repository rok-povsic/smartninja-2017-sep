from google.appengine.ext import ndb
from google.appengine.api import users, mail, taskqueue

from models.topic import Topic


class Comment(ndb.Model):
    user_email = ndb.StringProperty()
    content = ndb.TextProperty()
    topic_id = ndb.IntegerProperty()
    topic_title = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @staticmethod
    def create_comment(topic_id, text):
        email = users.get_current_user().email()
        topic = Topic.get_by_id(int(topic_id))
        comment = Comment(content=text, user_email=email,
                          topic_id=int(topic_id), topic_title=topic.title)
        comment.put()

        params = {
            "email": topic.user_email,
            "topic_title": topic.title,
            "topic_id": topic.key.id()
        }
        taskqueue.add(url="/task/email-topic-author",
                      params=params)