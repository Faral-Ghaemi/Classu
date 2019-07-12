from django.contrib.gis.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    slug = models.SlugField(unique=True,null = True, blank=True)
    image = models.ImageField(upload_to="images/category/", verbose_name="تصویر دوره")



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Cource(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="دسته بندی دوره")
    image = models.ImageField(upload_to="images/cources/", verbose_name="تصویر دوره")
    content = models.TextField(verbose_name="درباره دوره")
    teacher = models.CharField(max_length=200,verbose_name="نام مدرس")
    time = models.CharField(max_length=340,verbose_name="مدت دوره")
    school = models.CharField(max_length=290,verbose_name="نام آموزشگاه")
    address = models.CharField(max_length=500,verbose_name="آدرس آموزشگاه")
    price = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="هزینه دوره")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="نام کاربری")
    date = models.DateField(default=date.today(), verbose_name="تاریخ")
    date_start = models.DateField(verbose_name=" تاریخ شروع دوره")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Cource, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Amoozeshgah(models.Model):
    name = models.CharField(max_length=250,verbose_name="نام آموزشگاه")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی آموزش های آموزشگاه")
    mpoint = models.PointField()
    objects = models.GeoManager()
