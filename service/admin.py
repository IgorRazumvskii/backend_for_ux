from django.contrib import admin

from .models import Service, Client, Example, ClientService


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'info'
    )
    search_fields = ('img', 'name', 'price', 'info')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'name'
    )
    search_fields = ('number',)


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = (
        'service',
    )
    search_fields = ('service', )


@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    # Настроим отображение полей в админке
    list_display = (
        'client_name',  # Показать имя клиента
        'service_name',  # Показать имя услуги
        'date',  # Показать дату
    )

    # Позволяет искать по имени клиента, имени услуги и дате
    search_fields = ('client__name', 'service__name', 'date')

    # Дополнительные настройки
    list_filter = ('date',)





