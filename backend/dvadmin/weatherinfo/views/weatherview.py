from rest_framework import serializers

from dvadmin.utils.json_response import DetailResponse, SuccessResponse
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.system.models import WeatherInfo
from dvadmin.utils.serializers import CustomModelSerializer

# class WeatherInfoSerializer(CustomModelSerializer):
#     """
#     部门-序列化器
#     """
#     # temperature = serializers.
#     date_recorded = serializers.DateField()
    
#     def get_status_label(self, obj: Dept):
#         if obj.status:
#             return "启用"
#         return "禁用"

#     def get_has_children(self, obj: Dept):
#         return Dept.objects.filter(parent_id=obj.id).count()

#     class Meta:
#         model = Dept
#         fields = '__all__'
#         read_only_fields = ["id"]


# class WeatherInfoViewSet(CustomModelViewSet):
#     """
#     部门管理接口
#     list:查询
#     create:新增
#     update:修改
#     retrieve:单例
#     destroy:删除
#     """
#     queryset = WeatherInfo.objects.all()
#     # serializer_class = WeatherInfoSerializer
#     # create_serializer_class = WeatherInfoCreateUpdateSerializer
#     # update_serializer_class = WeatherInfoCreateUpdateSerializer
#     filter_fields = ['temperature', 'date_created']
#     search_fields = ['temperature']
#     # extra_filter_backends = []
#     # import_serializer_class = DeptImportSerializer
#     # import_field_dict = {
#     #     "name": "部门名称",
#     #     "key": "部门标识",
#     # }



def all_records(self, request, *args, **kwargs):
        self.extra_filter_backends = []

        queryset = self.filter_queryset(self.get_queryset())
        data = queryset.filter(status=True).order_by('date_created')
        return DetailResponse(data=data, msg="success")
