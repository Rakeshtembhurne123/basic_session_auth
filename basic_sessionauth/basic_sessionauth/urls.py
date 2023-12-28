"""withrestc4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from testapp import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)#ModelViewSet asala tr basename nahi liha lagat



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')), # session auth cha ve accounts/login logout hote
                                                            # template run hote aani username ani password vicharate....data takun login kela tari nahi disat manun setting madhe 'LOGIN_REDIRECT_URL='/api/' asa lihacha
                                                            #akda login rahala tr api/ lihila tari data disate...manun mg account/logout karacha mg logout hote
]
