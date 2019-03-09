from django import template

register = template.Library()

@register.filter(name='acut')
def acut(value,arg):
    """
    This cuts out all values of args from the string.
    """
    return value.replace(arg,'')

# register.filter('bcut',acut)
