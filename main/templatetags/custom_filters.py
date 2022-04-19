from django import template

register = template.Library()

@register.filter
def index(list, index):
    return list[index]

@register.filter
def split(object, character):
    new_list = list(filter(None, object.split(character)))
    return new_list