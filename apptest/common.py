#公共类
import hashlib
def md5(pwd):
     m = hashlib.md5(pwd.encode(encoding='utf-8'))
     return m.hexdigest()