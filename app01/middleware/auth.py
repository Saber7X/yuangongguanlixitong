from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    #     中间件1
    def process_request(self, request):
        # 获取URL
        if request.path_info in ["/login/", "/image/code/"]:
            return
        info_dict = request.session.get("info")  # 获取登录信息
        if info_dict:
            return
        return redirect("/login/")
