from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View,TemplateView
from .models import Banner
from django.contrib.sitemaps import Sitemap
from apps.posts.models import Post
from django.urls import reverse


class HomeView(View):
    template_name = "theme_lotus/pages/home.html"
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request,self.template_name,context)


class PhanHoaView(TemplateView):
    template_name = 'theme_lotus/pages/phan_hoa.html'
class SuaOngChuaView(TemplateView):
    template_name = 'theme_lotus/pages/sua_ong_chua.html'
class TinhBotNgheView(TemplateView):
    template_name = 'theme_lotus/pages/tinh_bot_nghe.html'
class BangGiaView(TemplateView):
    template_name = 'theme_lotus/pages/bang_gia.html'

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Post.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.updated

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'login_custom', 'signup_custom',
                'user_address','user_profile','logout_custom','post_list'
                ,'base_contact','base_introduction','base_payment','products',
                'orders','cart'
                ]

    def location(self, item):
        return reverse(item)


