from flask import Flask
from flask_admin import Admin as BaseAdmin, helpers
from flask_controller_bundle import url_for


class Admin(BaseAdmin):
    def init_app(self, app: Flask):
        self.name = app.config.get('ADMIN_NAME')
        self.subdomain = app.config.get('ADMIN_SUBDOMAIN')
        self._set_admin_index_view(app.config.get('ADMIN_INDEX_VIEW'),
                                   url=app.config.get('ADMIN_BASE_URL'))
        self.base_template = app.config.get('ADMIN_BASE_TEMPLATE')
        self.template_mode = app.config.get('ADMIN_TEMPLATE_MODE')
        super().init_app(app)
        app.context_processor(lambda: dict(admin_base_template=self.base_template,
                                           admin_view=self.index_view,
                                           h=helpers,
                                           get_url=url_for))

    def menu(self):
        return [item for item in super().menu() if item.name != 'Home']
