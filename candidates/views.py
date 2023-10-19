from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from candidates.serializers import CandidateSerializer, CandidateSerializerReadOnly
from candidates.models import Candidate
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

def home(request):
    #return render(request, 'users/home.html')
    return render(request, 'users/home.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the Streamlining Candidate Management index.")
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("candidates/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
@api_view(['GET'])
def candidates(request):

    data = Candidate.objects.all()
    serializer = CandidateSerializerReadOnly(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_candidate(request):

    serializer = CandidateSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)