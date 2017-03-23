
from django import template

from apps.pages.models import Setting

register = template.Library()




@register.simple_tag
def get_setting(name):
    setting = Setting.objects.first()
    if setting:
        if name == 'phone_hn':
            return setting.phone_hn
        if name == 'phone_sg':
            return setting.phone_sg
        if name == 'email':
            return setting.email
        if name == 'facebook':
            return setting.facebook
        if name == 'youtube':
            return setting.youtube
        if name == 'domain':
            return setting.domain
        if name == 'logo':
            return setting.logo.url
        if name == 'address_hn':
            return setting.address_hn
        if name == 'address_sg':
            return setting.address_sg
        if name == 'skype':
            return setting.skype
    return ''