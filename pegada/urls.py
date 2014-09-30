from django.conf.urls import patterns, include, url

from django.contrib import admin

from pegada.core.views import HomepageView

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomepageView.as_view()),
)
