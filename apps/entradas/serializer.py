
from rest_framework import serializers
from .models import Noticia, GaleriaNoticia


class GaleriaNoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = GaleriaNoticia
        fields = ('imagen',)


class NoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
    galeria = GaleriaNoticiaSerializers(many=True)




# class SeccionSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Seccion
#         fields = '__all__'
#     contenido = ContenidoSerializers(many=True)
    


