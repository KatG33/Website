"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# imports admin module to manage data through admin interface
from django.contrib import admin
# 'path' permits to define URL routes, 
# 'include' allows to include URL patterns from other components, 
#       like 'flashcards' into the main folder 'backend'
from django.urls import include, path
# 'urlpatterns' - list that stores all URLs. 
#       Each item in this list defines a URL pattern and
#       specifies which view or URL configuration should handle it
urlpatterns = [
    # To see admin interface, visit http://127.0.0.1:8000/admin/ in a browser
    path('admin/', admin.site.urls),
    # To look inside 'flashcards' component's configuration, 
    #       add flashcards/ at the end of a URL: http://127.0.0.1:8000/flashcards/
    # path('flashcards/', include('flashcards.urls')),
    path('', include('flashcards.urls')),
]
