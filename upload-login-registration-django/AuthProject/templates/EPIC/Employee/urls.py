from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    
    url(r'^registration/myprofile/$', myprofile, name='myprofile'),
    url(r'^registration/mycontact/$', mycontact, name='mycontact'),
    url(r'^registration/myid/$', myid, name='myid'),
    url(r'^registration/myfamily/$', myfamily, name='myfamily'),
    url(r'^registration/myacademic/$', myacademic, name='myacademic'),
    url(r'^registration/myexperiance/$', myexperiance, name='myexperiance'),
    url(r'^registration/account/$', account, name='account'),
    url(r'^registration/peopleknowsme/$', peopleknowsme, name='peopleknowsme'),
    url(r'^registration/staffknowsme/$', staffknowsme, name='staffknowsme'),
    url(r'^registration/thankyou/$', thankyou, name='thankyou'),
    
    # url(r'^fill-details/$', employee_fill_details, name='employee_fill_details'),
    # url(r'^new-employees/$', employee_new_employees, name='employee_new_employees'),
    
    # url(r'^upload/$', employeeupload, name='employeeupload'),
    # url(r'^quicksearch/$', quicksearchemployee, name='quicksearchemployee'),
    # url(r'^search/$', searchemployee, name='searchemployee'),
    # url(r'^details/([0-9,a-z]+)/$', employeedetails, name='employeedetails'),
    # url(r'^edit/([0-9,a-z]+)/$', employeeedit, name='employeeedit'),
    # url(r'^attachphoto/$', attachphoto, name='attachphoto'),
    
)
