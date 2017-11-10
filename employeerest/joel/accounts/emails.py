from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
class Emailcustomclass(object):
	def __init__(self, *args ,**kwargs):
		self.url = args[0]
		self.mail = args[1]
		subject, from_email, to = 'Email verification', '<---mailid here--->', self.mail
		text_content = 'Travidux'
		html_content = '<a href='+self.url+'>click here To Activate</a>'
		self.mail = EmailMultiAlternatives(subject, text_content, from_email, [to])
		self.mail.attach_alternative(html_content, "text/html")
		self.mail.send()
			# self.mail = EmailMessage(
			# 	subject='Email verification',
			# 	body='<a href='+self.url+'>click here To Activate</a>',
			# 	to=[self.mail],
			# 	reply_to=['joelhanson@travidux.com'],
			# 	headers={'Content-Type': 'text/plain'},
			# 	)
	# def emaildata(self,*args,**kwargs):
	# 	email = EmailMessage(
	# 		subject='Email verification',
	# 		body='<a href='+self.url+'>click here To Activate</a>',
	# 		to=[self.mail],
	# 		reply_to=['joelhanson@travidux.com'],
	# 		headers={'Content-Type': 'text/plain'},
	# 		)

		# email.send()
# '''
# subject, from_email, to = 'Email verification', 'joelhanson@travidux.com', self.mail
# text_content = 'Travidux'
# html_content = '<a href='+self.url+'>click here To Activate</a>'
# self.mail = EmailMultiAlternatives(subject, text_content, from_email, [to])
# self.mail.attach_alternative(html_content, "text/html")
#
#
#
# data = Emailcustomclass('http://0.0.0.0:8000/api/users/activate/list/5/','joelhanson025@gmail.com')
# '''
