"""
URL configuration for MagnetoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Agent import views as AgentViews
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AgentViews.home, name="Home"),
    path('about/', AgentViews.about, name="About"),
    path('chat/', AgentViews.chat, name="Chat"),
    path('registro/', AgentViews.registro, name="registro"),
    path('login/', AgentViews.login_view, name="Login"),
    path("api/chat/", AgentViews.chat_api, name="chat_api"),
    path('estadisticas/', AgentViews.estadisticas, name="estadisticas"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('personalidad/', AgentViews.personalidad, name="personalidad"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
