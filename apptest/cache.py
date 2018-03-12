#设置缓存
import memcache
#支持多个集群根据权重去对应集群中获取值
#mc = memcache.Client([('1.1.1.1:12000', 1), ('1.1.1.2:12000', 2), ('1.1.1.3:12000', 1)], debug=True)
class memcacheclass():
    def _init_(self):
        self.mc=memcache.Client([('127.0.0.1:8000')], debug=True)
    def setkey(self,k,v):
        mc=self.mc
        mc.set(k,v)
    def getvalue(self,k):
        mc=self.mc
        return  mc.get(k)
'''
mc = memcache.Client([('127.0.0.1:8000')], debug=True)
#修改值存在修改，不存在添加
mc.set('k1', 'v1')
val = mc.get('k1')

#添加纪录
mc.add('k2','v2')
mc.add('k2','v2')#报错
#如果memcache中存在kkkk，则替换成功，否则一场
# #替换值如果存在则修改，存在报异常
mc.replace('kkkk','999')
#设置多个键值对
mc.set_multi({'k3': 'v3', 'k4': 'v4'})
#删除值
mc.delete('k1')
#批量删除
mc.delete_multi(['k1', 'k2'])
#根据key获取值
val = mc.get('k1')
#批量获取值
item_dict = mc.get_multi(["k1", "k2", "k3"])
#根据key在value后面追加值
mc.append('k1', 'after')
# k1 = "v1after"
#根据key在value前面追加值
mc.prepend('k1', 'before')
# k1 = "beforev1after"
#incr，根据key将value的值自增1
mc.incr('k1')
#decr ，根据key将value的值自减1
mc.decr ('k1')
#为了避免多个用户同时修改提交数据导致数据不一致
mc = memcache.Client(['192.168.1.100:45555'],debug=True,cache_cas=True)
v = mc.gets('product_count')
print(v)
mc.cas('product_count','111')#报错
#gets与cas中间修改值得话会报错
mc.cas('product_count','889')
'''
