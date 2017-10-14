import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Example_Theme3Plugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'example_theme3')

    def form_template(context, data_dict):
        return u'templates/package/resource_edit.html'
