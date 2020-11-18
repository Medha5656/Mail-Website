from django.urls import path

from django.views.generic import TemplateView

from emailapp.views import *

urlpatterns=[
	path('index/',TemplateView.as_view(template_name='emailapp/index.html')),
	path('sendmail/',sendmail_view),
]
