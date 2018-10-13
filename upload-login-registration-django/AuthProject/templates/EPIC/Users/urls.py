from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    
    url(r'^register/$', register, name='register'),
    url(r'^email-verification/$', email_verification, name='email_verification'),   
    url(r'^mobile-verification/$', mobile_verification, name='mobile_verification'),    
    url(r'^change-password/$', change_password, name='change_password'),
    url(r'^signout/$', signout, name='signout'),    
    url(r'^forgot-password/$', forgot_password, name='forgot_password'),
    url(r'^reset-password/$', reset_password, name='reset_password'),
    
    # url(r'^tnc/$', tnc, name='tnc'),
    # url(r'^link-sent/$', link_sent, name='link_sent'),
    # url(r'^thank-you/$', thank_you, name='thank_you'),
        
)
