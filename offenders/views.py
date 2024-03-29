from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import OffenderProfileSerializer
from .models import OffenderProfile

# Create your views here.

class OffenderView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def get(self, request):
    queryset = OffenderProfile.objects.all()
    serializer = OffenderProfileSerializer(queryset, many=True)
    return Response(serializer.data)


  def post(self, request, *args, **kwargs):
    file_serializer = OffenderProfileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
