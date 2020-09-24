"""
Django views for chatbot project.

Created manually

"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from django.http import JsonResponse
from . import imdb, assistant
import requests
import json

serverState = 0
userResponse = []
robotResponse = []
userQuestions = {1:"Hello", 0:"I am tired", 2: "Give me some movies"}
assistant = assistant.Assistant()
assistant.create_session()

def hello(request):
  return JsonResponse({'response_text':'hello world!'})

@api_view(('GET',))
def get_movies(request):
    # request
    # response = requests.get('http://freegeoip.net/json/')
    response_data = imdb.get_imdb_movies()
    # geodata = response.json()
    return Response(
      data={"movieList":response_data}
    )

@api_view(('GET',))
def get_question(request):
    user_question = userQuestions[1] # assume greeting first
    robot_response = assistant.ask_assistant(user_question)

    # geodata = response.json()
    return Response(
      data={"questionString":robot_response,"questionCode":1}
    )


@api_view(['GET', 'POST'])
def post_answer(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
      response_data = list(range(10))
      # geodata = response.json()
      return Response(
        data=response_data
      )
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        print(type(data))
        userResponse.append(data)
        if int(data['questionCode']) in userQuestions:
          user_question = userQuestions[int(data['questionCode'])]
        print(user_question)

        # get response and movie list
        updatedMovieList = imdb.get_imdb_movies()
        robotMessage = assistant.ask_assistant(user_question)
        responseData = {"nextQuestionString": robotMessage,"nextQuestionCode": int(data['questionCode'])+1,"updatedMovieList" : updatedMovieList}
        return Response(
          data=responseData
          )
          