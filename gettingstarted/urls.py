from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
	url(r'^abstract', hello.views.abstract, name='abstract'),
	url(r'^underdevelopment', hello.views.underdevelopment, name='underdevelopment'),
	url(r'^sorry', hello.views.sorry, name='sorry'),
	url(r'^searchresults', hello.views.searchresults, name='searchresults'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_product', hello.views.search_product),
    url(r'^fetch_reviews', hello.views.fetch_reviews),
    url(r'^get_client_ip', hello.views.get_client_ip),
]
