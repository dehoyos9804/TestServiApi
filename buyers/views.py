from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import requests
from .models import Buyer
from .serializers import CreateBuyerSerializers
from .google_code import addressToLatLng

# Create your views here.
@api_view(['POST'])
def crear(request):
    try:
        #colocar los datos que vienen del request en el serializador
        serialize = CreateBuyerSerializers(data=request.data)
        # validamos la data
        if serialize.is_valid():
            # una vez que se compruebe que la data ha sido validada, se guarda
            serialize.save()

            return Response({
                'title': 'Success',
                'message': 'Comprador Creado Exitosamente'
            }, 200)

        return Response(serialize.errors)
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': e
        }
        return Response(json.loads(exception))

@api_view(['GET'])
def lista(request):
    try:
        if request.method == 'GET':
            #obtenemos todos los compradores
            buyers = Buyer.objects.all()

            #mapeamos los datos
            data = []
            for buyer in buyers:
                data.append({
                    'id': buyer.id,
                    'nombres': buyer.names,
                    'apellidos': buyer.surnames,
                    'direccion': buyer.address,
                    'ciudad': buyer.city,
                    'longitud': buyer.longitud,
                    'latitud': buyer.latitud
                })

            return Response({'data': data}, 200)

        return Response(
            {
                "error":"Http",
                "code": "405",
                "message": "Método no permitido"
            },
            405
        )
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': e
        }
        return Response(json.loads(exception))

@api_view(['GET'])
def usuario(request, pk):
    try:
        if request.method == 'GET':
            #obtenemos todos los compradores
            try:
                buyer = Buyer.objects.get(pk=pk)

            except Buyer.DoesNotExist:
                return Response({
                    'error': 'Model',
                    'message': 'No éxiste el recurso'
                })

            #mapeamos los datos
            data = {
                'id': buyer.id,
                'nombres': buyer.names,
                'apellidos': buyer.surnames,
                'direccion': buyer.address,
                'ciudad': buyer.city,
                'longitud': buyer.longitud,
                'latitud': buyer.latitud
            }

            return Response({'data': data}, 200)

        return Response(
            {
                "error":"Http",
                "code": "405",
                "message": "Método no permitido"
            },
            405
        )
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': 'No éxiste el recurso'
        }
        return Response(json.loads(exception))


@api_view(['DELETE'])
def delete_buyer(request, pk):
    try:
        if request.method == 'DELETE':
            # obtenemos todos los compradores
            try:
                buyer = Buyer.objects.get(pk=pk)

            except Buyer.DoesNotExist:
                return Response({
                    'error': 'Model',
                    'message': 'No éxiste el recurso'
                })

            # elimino el recurso
            buyer.delete()

            return Response({
                'title': 'Success',
                'message': 'Comprador eliminado'
            }, 200)

        return Response(
            {
                "error": "Http",
                "code": "405",
                "message": "Método no permitido"
            },
            405
        )
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': e
        }
        return Response(json.loads(exception))

@api_view(['GET'])
def geocodificar_base(request):
    try:
        if request.method == 'GET':
            # obtenemos todos los compradores que están en estado_geo 0
            try:
                buyers = Buyer.objects.filter(estado_geo='0')

            except Buyer.DoesNotExist:
                return Response({
                    'error': 'Model',
                    'message': 'No hay ningún para actualizar'
                })

            # elimino el recurso
            for buyer in buyers:
                #preparar direccion
                address = buyer.address + ', ' + buyer.city

                latlng = addressToLatLng(address)

                if not latlng:
                    buyer.latitud = 0
                    buyer.longitud = 0
                    buyer.save()
                else:
                    buyer.latitud = latlng.latlng[0]
                    buyer.longitud = latlng.latlng[1]
                    buyer.estado_geo = 1
                    buyer.save()

            return Response({
                'title': 'Success',
                'message': 'Datos Actualizados'
            }, 200)

        return Response(
            {
                "error": "Http",
                "code": "405",
                "message": "Método no permitido"
            },
            405
        )
    except Exception as e:
        exception = {
            'error': 'Exception',
            'Code': '500',
            'message': e
        }
        return Response(json.loads(exception))