from serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from authenticate.models import Employee
from rest_framework import status
import json,csv,re,os,datetime
from django.forms.models import model_to_dict


class LoginView(APIView):

        serializer_class = LoginSerializer
        permission_classes = (AllowAny,)

        def get_serializer_class(self):
            return self.serializer_class

        def post(self, request, format=None):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                try:
                    username = serializer.data['username']
                    password = serializer.data['password']
                    user_obj = Employee.objects.get(firstname=username,password=password)   
                    if user_obj:
                        que_user_ob=User.objects.filter(username=username,password=password)
                        if not que_user_ob:
                            user_ob=User.objects.create(username=username,password=password)
                        else:
                            user_ob=User.objects.get(username=username,password=password)

                        token = Token.objects.get_or_create(user=user_ob)
                        token_dict = model_to_dict(token[0])
                        token = token_dict.get('key')

                        return Response({'status':'OKAY','token':token},status=status.HTTP_200_OK)
                    else:
                        return Response({"PASSWORD_INVALID"}, status=400)
                except:
                    return Response({"PASSWORD_INVALID"}, status=400)
            else:
                return Response({"pattern"}, status=400)

class Registeration(APIView):
    serializer_class = Registernewuser
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_class

    def post(self,request,format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                firstname = serializer.data['firstname']
                lastname = serializer.data['lastname']
                email = serializer.data['email']
                password = serializer.data['password']
                mobile = serializer.data['mobile']
                print firstname , lastname
                user_obj = Employee.objects.filter(firstname=firstname,password=password)
                print user_obj
                if user_obj:
                    return Response({"exists"},status=200)
                else:
                    Employee.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,mobile=mobile)
                    return Response({"OKAY"},status=200)
            except Exception as e:
                print 'error',e
                return Response(status=400)
        else:
            return Response({"pattern"},status=400)

class UploadFile(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        bulk_data = []
        data = request.FILES.get('file',None)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        STATIC_ROOT = os.path.join(BASE_DIR, "static")
        file_name = STATIC_ROOT+'/'+str(date)+'_'+data.name

        data_file = csv.reader(data,delimiter=',')
        with open(file_name, 'w') as fp:
            a = csv.writer(fp, delimiter=',') 
            if data_file is not None:
                st1 = '0'
                st = '0'
                for i in data_file:
                    try:
                        emp = Employee.objects.get(firstname=i[0],password=i[4])
                    except:
                        csv_write = []
                        email = i[2]
                        mobile = i[3]
                        match_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
                        st=''
                        if not match_email:
                            st = 'invalid email'
                        match_mobile = re.search(r'(^[+0-9]{1,3})*([0-9]{10,11}$)',mobile)
                        if not match_mobile:
                            st = st+'//'+'invalid mobile'
                        if match_email and match_mobile:
                            Employee.objects.create(firstname=i[0],lastname=i[1],email=i[2],mobile=i[3],password=i[4])
                        i.append(st)
                        a.writerow(i)
                json = {"file":"static/"+data.name}
                return Response(json,status=200)

            else:
                return Response(status=400)

        
def rakesh():
    import time
    time.sleep(15)
    print 'rakesh'
