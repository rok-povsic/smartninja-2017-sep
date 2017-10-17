import random

from handlers.base import BaseHandler


class StockHandler(BaseHandler):
    def get(self):
        return self.write(random.randint(10, 20))