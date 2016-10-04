from django import template
from django.http import Http404

from ..models import BlogPost

register = template.Library()

def grouped(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

@register.simple_tag(takes_context=True)
def blogpost_list(context, group_size=0, published=True, num_items=10):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    qset = BlogPost.objects.language().filter(published=published)[(page-1)*num_items:num_items]
    if not group_size:
        return qset
    else:
        return grouped(qset, group_size)


@register.simple_tag(takes_context=True)
def blogpost(context, pk):
    try:
        item = BlogPost.objects.language().get(pk=pk)
    except BlogPost.DoesNotExist:
        raise Http404("Object not found!")
    return item
