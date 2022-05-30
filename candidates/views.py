from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from candidates.serializers import CandidateSerializer, CandidateSerializerReadOnly
from candidates.models import Candidate


@api_view(['GET'])
def candidates(request):
    # TODO: Add Pagination
    data = Candidate.objects.all()
    serializer = CandidateSerializerReadOnly(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_candidate(request):
    # TODO: Add remaining fields
    serializer = CandidateSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)