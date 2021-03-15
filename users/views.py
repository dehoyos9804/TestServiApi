from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from .serializers import CreateUserSerializer
import json

with open('./config.json', 'r') as file:
    config = json.load(file)
# Create your views here.
CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        # colocar los datos que vienen del request en el serializador
        serializar = CreateUserSerializer(data=request.data)

        #validamos la data
        if serializar.is_valid():
            #una vez que se compruebe que la data ha sido validada, se guarda
            serializar.save()
            return Response({
                'title':'Success',
                'message' : 'Usuario registrado exitosamente'
            }, 200)

        return Response(serializar.errors)

    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': e
        }
        return Response(json.loads(exception))

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        '''
            la entrada debe tener el siguiente formato
            {"username": "username", "password": "1234abcd"}
        '''
        r = requests.post('http://127.0.0.1:8000/o/token/',
                            data={
                                'grant_type': 'password',
                                'username': request.data['username'],
                                'password': request.data['password'],
                                'client_id': CLIENT_ID,'client_secret': CLIENT_SECRET,
                            }
                          )

        return Response(r.json())
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': str(e)
        }
        return Response(json.loads(exception))


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    try:
        '''
             la entrada debe tener el siguiente formato
            {"refresh_token": "<token>"}
        '''
        r = requests.post('http://127.0.0.1:8000/o/token/',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': str(e)
        }
        return Response(json.loads(exception))

@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    try:
        '''
            revoca el tokens.
            {"token": "<token>"}
         '''
        r = requests.post('http://127.0.0.1:8000/o/revoke_token/',
            data={
                'token': request.data['token'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        # If it goes well return sucess message (would be empty otherwise)
        if r.status_code == requests.codes.ok:
            return Response({'message': 'token revoked'}, r.status_code)
        # Return the error if it goes badly
        return Response(r.json(), r.status_code)
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': str(e)
        }
        return Response(json.loads(exception))
