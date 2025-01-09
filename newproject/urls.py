"""
URL configuration for newproject project.

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
from django.contrib import admin
from django.urls import path
from niranjana.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first",task_page, name="task_page"),
    path("view",task_view,name='view'),
    path("task_delete/<int:task_id>",task_delete,name="task_delete"),
    path("task_update/<int:task_id>",task_update,name="task_update"),

]
