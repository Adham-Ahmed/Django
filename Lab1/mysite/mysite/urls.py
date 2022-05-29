"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from todo.views import add_view, editFunction, home_view
from todo.views import item_view
from todo.views import item_view
from todo.views import edit_view
from todo.views import delete_view
from todo.views import addToArray_view
# from todo.views import home_view2
# from todo.views import nothing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('home/', home_view),
    path('home/view/<int:id>', item_view),
    path('home/edit/<int:id>', edit_view),
    path('editFunction/<int:id>', editFunction),
    path('home/delete/<int:id>', delete_view),
    path('home/add', add_view),
    path('home/addToArray', addToArray_view),
]
