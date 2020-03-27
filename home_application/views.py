# -*- coding: utf-8 -*-
import json
from base64 import b64encode

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from blueking.component.shortcuts import get_client_by_request
from config import *


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/index_home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')

# 组件调用sdk
def module_sdk(request):
    cookies = request.COOKIES
    client = get_client_by_request(request)
    print(client)
    print(cookies)
    kwargs = {
        'bk_app_code': APP_CODE,
        'bk_app_secret': SECRET_KEY,
        'bk_token': cookies.get('bk_token')
    }
    result = client.cc.get_operation_log(kwargs)
    print(result)
    return JsonResponse(result)


# 组件直接调用
def module_api(request):
    script = b64encode("""netstat -at""".encode()).decode()
    kwargs = {
        'bk_app_code': APP_CODE,
        'bk_app_secret': SECRET_KEY,
        'bk_token': request.COOKIES.get('bk_token'),
        'bk_biz_id': 3,
        'script_content': script,
        'account': 'root',
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.5.72"
            }
        ]
    }
    url = BK_URL + '/api/c/compapi/v2/job/fast_execute_script/'
    result = requests.post(url=url, data=json.dumps(kwargs)).json()
    print(result)
    return JsonResponse(result)