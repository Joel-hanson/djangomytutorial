from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
	return field.as_widget(attrs={"class":css})

@register.filter
def count_true(value):
	return value.count(True)
@register.filter
def remove_(value):
	x = value.split('_')
	if len(x)==2:
		z = x[0]+' '+x[1]
	else:
		z = x[0]
	return z
