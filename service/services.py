from .models import Service, Client, ClientService


def search_services():
    return Service.objects.filter()


def search_service(pk):
    return Service.objects.get(pk=pk)


def record(phone_number, service_pk, name):
    client, created = Client.objects.get_or_create(number=phone_number, defaults={'name': name})

    service = Service.objects.get(name=service_pk)

    ClientService.objects.create(client=client, service=service)

