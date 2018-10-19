"""shoepersonic URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from home.views import index
from accounts import urls as account_urls 
from django.urls import path, re_path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf.urls.static import static
from shop import urls as shop_urls
from cart import urls as cart_urls
from reviews import urls as review_urls
from checkout import urls as checkout_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include(account_urls)),
    path('shop/', include(shop_urls)),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('reviews/', include(review_urls)),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
