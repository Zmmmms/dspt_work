from django.db import models

# Create your models here.


'''
用户类属性说明;

firstname： 	昵称命名
lastname： 	昵称姓氏
email： 		邮箱地址，非重复约束
passwd: 	登陆密码
address： 	当前使用地址
city： 		所在地
createtime：	创建时间
uptime： 	最后行为时间
'''

class User( models.Model):
	first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)


    class Meta:
    	ordering = ('-createtime',)


    def __str__(self):
    	return 'NAME: {} vs email {};'.format(self.last_name, self.email)
