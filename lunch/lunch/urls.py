"""lunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from stores.views import store_list, store_detail
from pages.views import home

urlpatterns = [

    
    # local : http://localhost:8000/store/
    #url(r'^store/$', store_list, name='store_list'), # Casper_note : Move home from stores/views.py to pages/views.py
    # store detail, pk = primary key, which would pass to view function store_detail() in stores/views.py
    #url(r'^store/(?P<pk>\d+)/$', store_detail, name='store_detail'),
    
    url(r'^$', home, name='home'),
    url(r'^store/', include('stores.urls')),
    # local : http://localhost:8000/admin/
    # 這一行把 admin/ 下面的 URL 對應到 Django admin
    url(r'^admin/', include(admin.site.urls)),

]

