from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.Login.as_view(), name='login'),
    path("signup/",views.SignUp.as_view(),name='sign_up'),
    path("create_listing/",views.CreateListings.as_view(),name = 'create_listing'),
    path('post/', views.Stock.as_view(), name='stock_detail'),
    path('home/',views.Listings.as_view(),name = 'lisitngs'),
    path('logout/',views.Logout.as_view(),name = 'logout')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


