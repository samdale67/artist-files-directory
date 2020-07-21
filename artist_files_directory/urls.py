"""
artist_files_directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from collections_app import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('what-are-artist-files/', views.what_are_artist_files),
    path('collections/', include('collections_app.urls')),
    path('collectors/', include('collectors_app.urls')),
    # User stuff
    path('', include('django.contrib.auth.urls')),
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'),
         name='register-success'),
    path('register/', views.register, name='register'),
    path('user/content/', views.user_content),
    path('user/edit/', views.user_edit, name='user-edit'),
    path('user/change-password/', views.change_password, name='change_password'),
    path('user/reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('user/reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset-password/confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/reset-password/complete', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
