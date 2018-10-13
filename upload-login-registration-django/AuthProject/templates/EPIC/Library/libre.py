from uuid import getnode
from subprocess import Popen, PIPE
import re


# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def get_client_mac(IP):
	mac = None
	# if IP != '127.0.0.1':
	pid = Popen(["arp", "-n", IP], stdout=PIPE)
	s = pid.communicate()[0]
	search = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
	if search:
		mac = search.groups()[0]
	return mac