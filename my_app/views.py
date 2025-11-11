from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serialziers import PersonModelSerializer

class PersonListApiView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonModelSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PersonCreateApiView(APIView):
    def post(self, request):
        serializer = PersonModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)