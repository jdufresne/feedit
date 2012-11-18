from django import template

register = template.Library()

@register.inclusion_tag('feeds/tags/sidebar.html')
def sidebar(user):
    return {'user': user}


@register.inclusion_tag('feeds/tags/feed_link.html')
def feed_link(user, feed):
    return {'feed': feed, 'unread': feed.unread_by(user).count()}
