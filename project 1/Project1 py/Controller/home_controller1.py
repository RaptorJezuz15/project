# For any request not pertaining to a specific model.


def route(app):
    @app.route("/")
    def hello():
        return "Welcome to Keith's Project one"


