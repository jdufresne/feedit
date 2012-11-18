from django import template

register = template.Library()

@register.inclusion_tag('feeds/tags/sidebar.html')
def sidebar(user):
    return {'user': user}
