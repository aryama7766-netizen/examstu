from django.shortcuts import render
from student_app.models import student,User
from student_app.serializer import studentserializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet



class SignupView(APIView):

 def  post(self, request):
     ser = User(data=request.data)

     if ser.is_valid():
            ser.save()
            return Response(
                {"msg": "User created successfully", "data": ser.data},
                status=status.HTTP_201_CREATED)

            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



class studentView(APIView):
   def post(self, request, *args, **kwargs):
    dser = studentserializer(data=request.data)
    if dser.is_valid():
        dser.save()
        return Response(data=dser.data, status=status.HTTP_201_CREATED)

    return Response(data=dser.errors, status=status.HTTP_400_BAD_REQUEST)


class studentViewSet(ViewSet):


 def post(self, request, *args, **kwargs):
    dser = studentserializer(data=request.data)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    if dser.is_valid():
        dser.save()
        return Response(data=dser.data, status=status.HTTP_201_CREATED)

    return Response(data=dser.errors, status=status.HTTP_400_BAD_REQUEST)

def get(self, request, *args, **kwargs):
    stu = student.objects.all()
    ser = studentserializer(stu, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)


class studentByidView(APIView):


 def get(self, request, sid):
    stu = student.objects.get(id=sid)
    ser = studentserializer(stu)
    return Response(data=ser.data, status=status.HTTP_200_OK)

def put(self, request, sid):
    stu = student.objects.get(id=sid)
    dser = studentserializer(data=request.data, instance=stu)

    if dser.is_valid():
        dser.save()
        return Response(data=dser.data, status=status.HTTP_200_OK)

    return Response(data=dser.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, sid):
    student.objects.get(id=sid).delete()
    return Response(data={"msg": "deleted"}, status=status.HTTP_200_OK)

