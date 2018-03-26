#测试 celery+redis+rabbitmq
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
r.set('hello','world')
print(r.get('hello'))
'''


from django.http import HttpResponse
'''
def tasks(request):
    print('before run_test_suit')
    result = run_test_suit.delay('110')
    print('after run_test_suit')
    return HttpResponse("job is runing background~")

'''




