from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
	"""
	The cut out all values
	"""
	return value.replace(arg,'')
# register.filter('cut',cut)


# using decorator
