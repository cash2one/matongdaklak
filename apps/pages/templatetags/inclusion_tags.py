
from django import template
from apps.posts.models import Post
from apps.pages.models import Page

register = template.Library()


@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_head_menu.html')
def head_menu():
    return {}
@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_order_form.html')
def order_form():
    return {}

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_latest_post.html')
def latest_post():
    posts = Post.objects.filter(active=True).order_by('-timestamp')[:6]
    return {'posts':posts}

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_seo.html')
def seo_page(page):
    page = Page.objects.filter(page=page).first()
    return {'object':page}

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_seo.html')
def seo_post(object):
    return {'object':object}

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_page.html')
def page(page):
    page = Page.objects.filter(page=page).first()
    return {'page':page}


