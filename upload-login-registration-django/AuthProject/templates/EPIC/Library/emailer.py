from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.conf import settings
import traceback
import urllib


# other imports




def account_created_emailer(data):
	try:
		subject = 'Ecom Express'
		message = '''

			<table width="100%" style="background-color: #ddd;">
				<tr>
					<td align="center">
						<table style="background-color: #fff; margin: 50px; padding: 20px; border: 1px solid #aaa; font-size: 12px; max-width: 500px;">
							<tr>
								<td align="left">
									<h3 style="color: #0072C6;">Congratulations Mr./Ms. '''+ data['name'] +''',</h3><br>
									<p style="color: #333333;">Your account has been created with <b>Ecom Express</b>. To login to your account please click on below link. </p><br><br>
									<a style="color: #18A689;" href="'''+ data['url'] +'''">'''+ data['url'] +'''</a><br><br><br>
									<p style="color: #333333;">Username :  <b>Email/Mobile</b><br>Password : <b>Mobile Number</b></p><br><br><br>
									<i style="color: #F87A6E;">Note: This is electronics transmited message. Please don't share this information with any body.</i><br><br><br>
									<span style="color: #888; font-style: italic; font-size: 12px;">.........<br>Regards,<br>
									<b>Ecom Express</b></span>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>		

		'''
		
		to = [data['email']]
		html_content = message 
		msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, to)
		msg.attach_alternative(html_content, "text/html")	
		msg.send()

	except:
		traceback.print_exc()
		pass

	return None





def email_verification_emailer(data):
	try:
		subject = 'Email Verification'
		message = '''

			<table width="100%" style="background-color: #ddd;">
				<tr>
					<td align="center">
						<table style="background-color: #fff; margin: 50px; padding: 20px; border: 1px solid #aaa; font-size: 12px; max-width: 500px;">
							<tr>
								<td align="left">
									<h3 style="color: #0072C6;">Hi Mr./Ms. '''+ data['name'] +''',</h3><br>
									<p style="color: #333333; text-align: justify;">Your account has been created with <b>Ecom Express</b>. Please verify your email address by click on below link. </p><br><br>
									<a style="color: #18A689;" href="'''+ data['link'] +'''">'''+ data['link'] +'''</a><br><br><br><br>
									<i style="color: #F87A6E;">Note: Your email and mobile must be verified before login.</i><br><br><br>
									<span style="color: #888; font-style: italic; font-size: 12px;">.........<br>Regards,<br>
									<b>Ecom Express</b></span>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>	

		'''
		
		to = [data['email']]
		html_content = message 
		msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, to)
		msg.attach_alternative(html_content, "text/html")	
		msg.send()

	except:
		traceback.print_exc()
		pass

	return None



def email_verification_done_emailer(data):
	try:
		subject = 'Email Verified'
		message = '''

			<table width="100%" style="background-color: #ddd;">
				<tr>
					<td align="center">
						<table style="background-color: #fff; margin: 50px; padding: 20px; border: 1px solid #aaa; font-size: 12px; max-width: 500px;">
							<tr>
								<td align="left">
									<h3 style="color: #0072C6;">Hi '''+ data['name'] +''',</h3><br>
									<p style="color: #333;">Your email has been varified successfully with <b>Ecom Express</b>. To login to your account please click on below link. </p><br><br>
									<a style="color: #18A689;" href="'''+ data['url'] +'''">'''+ data['url'] +'''</a><br><br><br><br>
									<i style="color: #F87A6E;">Note: Your email and mobile must be verified before login.</i><br><br><br>
									<span style="color: #888; font-style: italic; font-size: 12px;">.........<br>Regards,<br>
									<b>Ecom Express</b></span>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>	

		'''
		
		to = [data['email']]
		html_content = message 
		msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, to)
		msg.attach_alternative(html_content, "text/html")	
		msg.send()

	except:
		traceback.print_exc()
		pass

	return None




def forgot_password_emailer(data):
	try:
		subject = 'Password Reset'
		message = '''

			<table width="100%" style="background-color: #ddd;">
				<tr>
					<td align="center">
						<table width="70%" style="background-color: #fff; margin: 50px; padding: 20px; border: 1px solid #aaa;">
							<tr>
								<td>
									<h3>Hi '''+ data['name'] +''',</h3><br>
									Click on below link to reset your password:<br><br>
									<a href="'''+ data['link'] +'''">'''+ data['link'] +'''</a><br><br>
									<i>Note: This link is valid for 24 hours only.</i>
									<br><br><br><br>
									<span style="color: #888; font-style: italic;">.........<br>Regards,<br>
									<b>Ecom Express</b></span>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>	

		'''
		
		to = [data['email']]
		html_content = message 
		msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, to)
		msg.attach_alternative(html_content, "text/html")	
		msg.send()

	except:
		# traceback.print_exc()
		pass

	return None
