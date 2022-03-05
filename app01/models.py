from django.db import models


# Create your models here.

class Department(models.Model):
    # 部门表

    # id = models.CharField(verbose_name="id", max_length=32, primary_key=True)
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    # 员工表
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="用户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")

    # 有约束     写这种约束类型自动生成_约束的那一列的名字"_id" 这种约束的意思是根据别的表里的数据来约束这个表
    #           比如这个里面这一列只能是id里有的数据                    级联删除，如果所关联的那个部门没有了，这个员工也会被删除
    #                           根据哪张表        根据哪一列

    # 或者 是关联的那一列删除了，那么这一列就为空，和级联删除同理，但是要先设置为空
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", null=True, blank=True,
                               on_delete=models.SET_NULL)

    # 在 Django 中的约束
    gender_choices = (  # 新建选择字段
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNum(models.Model):
    # 靓号表
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)

    stauts_choices = (
        (1, "已占用"),
        (2, "未占用"),
    )
    stauts = models.SmallIntegerField(verbose_name="状态", choices=stauts_choices, default=2)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Task(models.Model):
    # 任务
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息", max_length=128)

    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)


class Boss(models.Model):
    # 老板
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄", max_length=128)
    img = models.CharField(verbose_name="头像", max_length=128)

class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='city/')