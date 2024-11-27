from django.db import models


class Service(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    info = models.CharField(max_length=50)
    text = models.TextField(default='')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, default='None')
    number = models.IntegerField()

    def __str__(self):
        return self.name


class ClientService(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     unique_together = ('client', 'service')

    @property
    def client_name(self):
        return self.client.name

    @property
    def service_name(self):
        return self.service.name


class Example(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT)


class Image(models.Model):
    example = models.ForeignKey(Example, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='images/')


