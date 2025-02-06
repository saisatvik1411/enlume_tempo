from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TimeEntry
from .serializers import TimeEntrySerializer

@api_view(['POST'])
def log_time(request):
    serializer = TimeEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Time logged successfully"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def generate_report(request, month):
    entries = TimeEntry.objects.filter(date__startswith=month)
    serializer = TimeEntrySerializer(entries, many=True)
    return Response(serializer.data)
