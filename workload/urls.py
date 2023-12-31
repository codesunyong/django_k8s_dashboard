from django.urls import path, re_path, include
from workload import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('^deployment/$', views.deployment, name="deployment"),
    re_path('^deployment_api/$', views.deployment_api, name="deployment_api"),
    re_path('^daemonset/$', views.daemonset, name="daemonset"),
    re_path('^statefulset/$', views.statefulset, name="statefulset"),
    re_path('^pod/$', views.pod, name="pod"),

]
