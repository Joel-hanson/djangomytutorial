from django import template

register = template.Library()

def cut(value,arg):
	"""
	The cut out all values
	"""
	return value.replace(arg,'')
register.filter('cut',cut)
