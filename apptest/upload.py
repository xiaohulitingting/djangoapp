#上传图片
from django.shortcuts import render, HttpResponse
import os,time

def test(request):
    return render(request, 'uploadimage.html')
#页面上传
def upload_avatar(request):
    file_obj = request.FILES.get('avatar')
    is_img = file_obj.name.split('.')[-1]
    if is_img not in ('jpeg', 'jpg', 'png', 'gif', 'tmp'):
        return HttpResponse("")
    t = time.time()
    timedate = int(round(t * 1000))
    name=str(timedate)+"."+is_img
    file_path = os.path.join('static\images', name)

    with open(file_path, 'wb') as f:# #将客户端上传的文件保存在服务器上，一定要用wb二进制方式写入，否则文件会乱码
        for chunk in file_obj.chunks():#通过chunks分片上传存储在服务器内存中,以64k为一组，循环写入到服务器中、、分片是为了充分利用网络带宽，加快上传速度
            f.write(chunk)
    return HttpResponse(file_path)
#https://segmentfault.com/a/1190000006909562
def upload_app(request):
    stream=request.POST.get("fileData")
    bytestream=bytes(stream, encoding='utf-8')