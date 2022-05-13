from django import template
from movies.models import MyList

register = template.Library()


@register.filter
def is_added(movie, user):
    return MyList.objects.filter(user=user, movie=movie).exists()
