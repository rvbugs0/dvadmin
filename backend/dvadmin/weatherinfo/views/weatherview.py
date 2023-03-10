from rest_framework import serializers
from rest_framework.response import Response
from dvadmin.utils.json_response import DetailResponse, SuccessResponse


from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.system.models import WeatherInfo
from django.http import HttpResponse

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from dvadmin.utils.serializers import CustomModelSerializer


class WeatherInfoSerializer(CustomModelSerializer):
    """
    接口白名单-序列化器
    """
    temperature = serializers.FloatField(required=True)
    date_recorded = serializers.DateField(required=True)

    class Meta:
        model = WeatherInfo
        fields = "__all__"
        read_only_fields = ["id"]



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


# view set has all the basic apis and custom api's are addded below and their urls also added in the urls.py


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def all_records(request):
    # WeatherInfo.objects.create(temperature = float("29.0"), date_recorded="2022-11-20")
    queryset = WeatherInfo.objects.all()
    read_serializer = WeatherInfoSerializer(queryset, many=True)
    return Response(read_serializer.data)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_by_range(request):
    to_date = request.GET["to_date"]
    from_date = request.GET["from_date"]
    queryset = WeatherInfo.objects.filter(date_recorded__range=(
        from_date, to_date)).order_by("date_recorded")
    read_serializer = WeatherInfoSerializer(queryset, many=True)
    return Response(read_serializer.data)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def average_temperatures(request):
    # queryset = WeatherInfo.objects.all()
    # read_serializer = WeatherInfoSerializer(queryset, many=True)
    # return Response(read_serializer.data)
    months = ['Jan', 'Feb', 'March', 'April', 'May',
              'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    data = WeatherInfo.objects.all()
    monthlyData = [[0] for i in range(12)]
    for i in data:
        dt = int(str(i.date_recorded).split("-")[1])
        monthlyData[dt-1].append(i.temperature)

    res = "["
    for i in range(len(monthlyData)-1):
        if (len(monthlyData[i])-1 > 0):
            res += "{\"month\":\""
            res += months[i]
            res += "\",\"average_temp\":"
            res += str(sum(monthlyData[i]) / (len(monthlyData[i])-1))
            res += "},"
    if (len(monthlyData[11]) > 1):
        res += "{\"month\":\""
        res += months[11]
        res += "\",\"average_temp\":"
        res += str(sum(monthlyData[11]) / (len(monthlyData[11])-1))
        res += "}"
    else:
        res = res[:len(res)-1]

    res += "]"
    return HttpResponse(res, content_type="application/json")
