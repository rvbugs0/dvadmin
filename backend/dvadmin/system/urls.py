from django.urls import path
from rest_framework import routers

from dvadmin.system.views.api_white_list import ApiWhiteListViewSet
from dvadmin.system.views.area import AreaViewSet
from dvadmin.system.views.dept import DeptViewSet
from dvadmin.system.views.dictionary import DictionaryViewSet
from dvadmin.system.views.file_list import FileViewSet
from dvadmin.system.views.login_log import LoginLogViewSet
from dvadmin.system.views.menu import MenuViewSet
from dvadmin.system.views.menu_button import MenuButtonViewSet
from dvadmin.system.views.message_center import MessageCenterViewSet
from dvadmin.system.views.operation_log import OperationLogViewSet
from dvadmin.system.views.role import RoleViewSet
from dvadmin.system.views.system_config import SystemConfigViewSet
from dvadmin.system.views.user import UserViewSet

# ---------------------
from dvadmin.weatherinfo.views.weatherview import *

from dvadmin.sensorydata.views.sensory_data_view import *

system_url = routers.SimpleRouter()
system_url.register(r'menu', MenuViewSet)
system_url.register(r'menu_button', MenuButtonViewSet)
system_url.register(r'role', RoleViewSet)
system_url.register(r'dept', DeptViewSet)
system_url.register(r'user', UserViewSet)
system_url.register(r'operation_log', OperationLogViewSet)
system_url.register(r'dictionary', DictionaryViewSet)
system_url.register(r'area', AreaViewSet)
system_url.register(r'file', FileViewSet)
system_url.register(r'api_white_list', ApiWhiteListViewSet)
system_url.register(r'system_config', SystemConfigViewSet)
system_url.register(r'message_center', MessageCenterViewSet)

system_url.register(r'weatherinfo',WeatherInfoViewSet)
system_url.register(r'SensoryData',SensoryDataViewSet)



urlpatterns = [
    path('user/export/', UserViewSet.as_view({'post': 'export_data', })),
    path('user/import/',
         UserViewSet.as_view({'get': 'import_data', 'post': 'import_data'})),
    path('system_config/save_content/',
         SystemConfigViewSet.as_view({'put': 'save_content'})),
    path('system_config/get_association_table/',
         SystemConfigViewSet.as_view({'get': 'get_association_table'})),
    path('system_config/get_table_data/<int:pk>/',
         SystemConfigViewSet.as_view({'get': 'get_table_data'})),
    path('system_config/get_relation_info/',
         SystemConfigViewSet.as_view({'get': 'get_relation_info'})),
    path('login_log/', LoginLogViewSet.as_view({'get': 'list'})),
    path('login_log/<int:pk>/', LoginLogViewSet.as_view({'get': 'retrieve'})),
    path('dept_lazy_tree/', DeptViewSet.as_view({'get': 'dept_lazy_tree'})),


    path('weatherinfo/all_records/', all_records),
    path('weatherinfo/get_average_temperatures/', average_temperatures),
    path('weatherinfo/get_by_range/', get_by_range)

]
urlpatterns += system_url.urls
