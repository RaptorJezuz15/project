# Front Controller design pattern - use a single controller as a point of entry into Our application.
# The front controller will then designate the flow of control to the appropriate controller.
from Controller import home_controller1, Employee_controller, Reimburstment_controller


def route(app):
    # Call all other controllers
    home_controller1.route(app)
    Employee_controller.route(app)
    Reimburstment_controller.route(app)


