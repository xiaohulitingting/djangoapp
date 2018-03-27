#coding:utf-8
#异步任务处理

from django.http import JsonResponse
from apptest.tasks import add
from myprojecttest.celery import app
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def get_add(request):
    s=add.delay(2,6)
    return JsonResponse({"job_id":s.id,"job_result":s.get()})#
@csrf_exempt
def get_status(request):
    job_id=request.GET.get("id")
    return JsonResponse({"task_status":app.AsyncResult(job_id).state,"task_result":app.AsyncResult(job_id).result})



