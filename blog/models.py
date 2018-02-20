from django.db import models
from django.utils import timezone


class Post(models.Model):
    #definicao de modelo
    #class esta definindo um objeto.
    #Post é o nome do nosso modelo
    #models.Model significa que o Post é um modelo de Django

    #definicao de propriedades do modelo
    author = models.ForeignKey('auth.User',  on_delete=models.CASCADE,)

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #models.CharField - define um texto com um número limitado de caracteres.
    #models.TextField - este é para textos longos, sem um limite
    #models.DateTimeField - este é uma data e hora.
    #models.ForeignKey - este é um link para outro modelo.
    # mais info : https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
