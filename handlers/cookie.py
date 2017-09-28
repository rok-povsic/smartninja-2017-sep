from handlers.base import BaseHandler


class CookieHandler(BaseHandler):
    def post(self):
        # Logika.
        self.response.set_cookie("piskotek", "nastavljen")
        return self.redirect('/')

