from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=128, db_index=True, verbose_name="Название категории")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_title

    class Meta:
        ordering = ('category_title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Detail(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    available = models.BooleanField(default=True, verbose_name="В наличии")
    country = models.CharField(max_length=128, verbose_name="Страна производства")
    description = models.TextField(max_length=2048, verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость товара")
    detail_title = models.CharField(max_length=1024, db_index=True, verbose_name="Название товара")
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name="Фотография товара")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detail_title

    class Meta:
        ordering = ('detail_title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
