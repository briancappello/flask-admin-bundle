from flask_controller_bundle import controller, rule

from .views import AdminSecurityController


routes = [
    controller('/admin', AdminSecurityController, rules=[
        rule('/login', 'login', endpoint='admin.login'),
        rule('/logout', 'logout', endpoint='admin.logout'),
    ]),
]
