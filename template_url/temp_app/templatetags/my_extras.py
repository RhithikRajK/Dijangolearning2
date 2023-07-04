from django import template

register = template.library()

def cut(value,arg):
    return value.replace(arg,' ')

register.filter('cut',cut)
