from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt

from .services import search_services, search_service, record
from .serializer import ServiceSerializer


@api_view(['GET'])
def output_services(request):
    services = search_services()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def output_service(request, pk):
    services = search_service(pk)
    serializer = ServiceSerializer(services)
    return Response(serializer.data)


@api_view(['POST'])
def create_record(request):
    try:

        service_id = request.data.get('service_id')
        phone_number = request.data.get('phone_number')
        name = request.data.get('name')

        if not service_id or not phone_number or not name:
            return Response({'error': 'Все поля обязательны: имя, номер телефона, услуга'}, status=400)

        record(phone_number, service_id, name)

        return Response({'message': 'Запись успешно создана'}, status=201)

    except ObjectDoesNotExist as e:
        return Response({'error': 'Указанная услуга не найдена'}, status=404)




