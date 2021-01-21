from django.conf.urls import url, include
from django.contrib import admin
from myquiz import views as index_views
from rest_framework.urlpatterns import format_suffix_patterns
from quizapi import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
	url(r'^$', index_views.index),
	url(r'^login/$', index_views.login),
	url(r'^questions/', include('quiz.urls')),
	url(r'^quizapi/', views.QuizApiList.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?p<path>.*)$', serve,{'document_root':   setting.MEDIA_ROOT}),
    url(r'^static/(?p<path>.*)$', serve,{'document_root':   setting.STATIC_ROOT}),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=setting.MEDIA_ROOT)
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=setting.STATIC_ROOT)