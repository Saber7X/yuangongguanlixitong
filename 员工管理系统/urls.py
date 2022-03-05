"""员工管理系统 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),

    # media
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),  # 固定写法    # 部门管理

    path('', views.aa),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    #           就是说这边必须包含一个数字
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('depart/multi/', views.depart_multi),

    # 用户管理
    path('user/list/', views.user_list),
    path('user/model/form/add/', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delate/', views.user_delate),

    # 靓号管理
    path('pretty/list/', views.pretty_list),
    path('pretty/add/', views.pretty_add),
    path('pretty/<int:nid>/edit/', views.pretty_edit),
    path('pretty/<int:nid>/delate/', views.pretty_delate),

    # """管理员"""
    path('admin/list/', views.admin_list),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/<int:nid>/delete/', views.admin_delete),
    path('admin/<int:nid>/reset/', views.admin_reset),

    #   登录
    path('login/', views.login),
    path('logout/', views.logout),
    path('image/code/', views.image_code),

    #     任务管理
    path('task/list/', views.task_list),
    path('task/add/', views.task_add),
    path('task/ajax/', views.task_ajax),

    #     订单管理
    path('order/list/', views.order_list),
    path('order/add/', views.order_add),
    path('order/delete/', views.order_delete),
    path('order/detail/', views.order_detail),
    path('order/edit/', views.order_edit),
    path('chart/list/', views.chart_list),
    path('chart/bar/', views.chart_bar),

    #     上传文件
    path('upload/list/', views.upload_list),
    path('upload/form/', views.upload_form),
    path('upload/modelform/', views.upload_modelform),

    # 城市
    path('city/list/', views.city_list)

]
