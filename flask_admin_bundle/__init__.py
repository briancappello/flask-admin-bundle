"""
    flask_admin_bundle
    ~~~~~~~~~~~~~~~~~~

    Integrates Flask Admin with Flask Unchained

    :copyright: Copyright © 2018 Brian Cappello
    :license: MIT, see LICENSE for details
"""

__version__ = '0.1.1'


from flask_unchained import Bundle

from .extensions import Admin
from .model_admin import ModelAdmin
from .macro import macro
from .security import AdminSecurityMixin
from .views import AdminDashboardView


class FlaskAdminBundle(Bundle):
    @classmethod
    def before_init_app(cls, app):
        pass

    @classmethod
    def after_init_app(cls, app):
        pass
