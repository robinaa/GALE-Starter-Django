{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import eb_worker

urlpatterns = [
    url(r'^$', eb_worker.index, name='index'),
]
{% else %}
# If you are not using celery/tasks, you can remove this app
{% endif %}
