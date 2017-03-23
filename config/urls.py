from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.pages.views import (
    HomeView,
    MatOngView,
    PhanHoaView,
    SuaOngChuaView,
    TinhBotNgheView,
    BangGiaView
)

from allauth.account.views import LogoutView
from apps.posts.views import PostDetailView, PostListView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from apps.pages.views import PostSitemap,StaticSitemap

sitemaps = {
    'post':PostSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


    url(r'^bai-viet/$', PostListView.as_view(), name='post_list'),
    url(r'^bai-viet/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),

    url(r'^mat-ong/$', MatOngView.as_view(), name='mat_ong'),
    url(r'^phan-hoa/$', PhanHoaView.as_view(), name='phan_hoa'),
    url(r'^sua-ong-chua/$', SuaOngChuaView.as_view(), name='sua_ong_chua'),
    url(r'^tinh-bot-nghe/$', TinhBotNgheView.as_view(), name='tinh_bot_nghe'),
    url(r'^bang-gia/$', BangGiaView.as_view(), name='bang_gia'),


    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
import debug_toolbar

urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
