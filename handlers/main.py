from handlers.base import BaseHandler
from models.topic import Topic


class MainHandler(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.deleted == False).fetch()
        return self.render_template("home.html", {"topics": topics})

