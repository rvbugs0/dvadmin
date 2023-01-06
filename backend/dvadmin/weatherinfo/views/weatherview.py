from rest_framework import serializers
from rest_framework.response import Response
from dvadmin.utils.json_response import DetailResponse, SuccessResponse


from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.system.models import WeatherInfo
from django.http import HttpResponse

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer



class WeatherInfoSerializer(serializers.ModelSerializer):
    temperature = serializers.FloatField(required=True)
    date_recorded = serializers.DateField(required=True)
    class Meta:
        model = WeatherInfo
        fields = ['temperature','date_recorded']
        read_only_fields = ["id"]

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def all_records(request):
    # WeatherInfo.objects.create(temperature = float("29.0"), date_recorded="2022-11-20")
    queryset = WeatherInfo.objects.all()
    read_serializer = WeatherInfoSerializer(queryset, many=True)
    return Response(read_serializer.data)
    




# def create(self, validated_data):
#     # Once the request data has been validated, we can create a todo item instance in the database
#     return WeatherInfo.objects.create(
#       temperature=validated_data.get('temperature'),
#       date_recorded = validated_data.get('date_recorded')
#     )

class WeatherInfoViewSet(CustomModelViewSet):
    """
    部门管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = WeatherInfo.objects.all()
    serializer_class = WeatherInfoSerializer
    filter_fields = ['temperature', 'date_recorded']
    search_fields = ['temperature']


