
from django.conf.urls import url, include
from rest_framework import routers
from cumlaudeUcla import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Estudiantes', views.EstudianteViewSet)

urlpatterns = [ 
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]