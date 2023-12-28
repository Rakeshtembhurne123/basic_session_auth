from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly






# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # authentication_classes = [BasicAuthentication,]
    # permission_classes = [IsAuthenticated,]

    #user pass takala tr sarv CRUD operation hote
    # pratek req. chya vedes user pass vicharate
    #http://www.utilities-online.info/base64/#.XFGE8lUzbIU
    # command--> http http://localhost:8000/api/ "authorization:Basic ZHVyZ2E6ZHVyZ2ExMjM="
    # postman--> Headers Section: Key: Authorization value: Basic ZHVyZ2E6ZHVyZ2ExMjM=
    #Authorization Section: Type: Basic Auth (select from dropdown list)Username: durga Password: durga123



    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]