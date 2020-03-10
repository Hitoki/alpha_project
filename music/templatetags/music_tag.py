from django import template

register = template.Library()


@register.filter
def lower(value, *args, **kwargs):
    return value.lower()


@register.filter
def upper(value):
    return value.upper()


register.simple_tag(lambda x: x - 1, name='minusone')

@register.simple_tag(name='minustwo')
def some_function(value):
    return value - 2
