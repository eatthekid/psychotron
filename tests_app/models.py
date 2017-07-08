from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    testName = models.CharField(verbose_name='Название теста',max_length=50, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=500, blank=True)
    url = models.URLField()

# Тест темперамента Айзенка
class EPI(models.Model):
    TestUser = models.ForeignKey(User, verbose_name='Тестируемый юзер')
    passingDate = models.DateTimeField(verbose_name='Дата прохождения теста', auto_now=True, auto_now_add=False)
    EXT = models.IntegerField(verbose_name="Экстраверсия")
    NER = models.IntegerField(verbose_name="Нейротизм")
    LIE = models.IntegerField(verbose_name="Шкала лжи")

# Тест структуры интеллекта Амтхауэра
class IST(models.Model):
    TestUser = models.ForeignKey(User, verbose_name='Тестируемый юзер')
    idPassing = models.IntegerField(verbose_name="id прохождения теста")
    passingDate = models.DateTimeField(verbose_name='Дата прохождения теста', auto_now=True, auto_now_add=False)
    DP = models.IntegerField(verbose_name="Дополнение предложений")
    IS = models.IntegerField(verbose_name="Исключение слова")
    AN = models.IntegerField(verbose_name="Аналогии")
    OB = models.IntegerField(verbose_name="Обобщение")
    AZ = models.IntegerField(verbose_name="Арефметические задачи")
    CR = models.IntegerField(verbose_name="Числовые ряды")
    PV = models.IntegerField(verbose_name="Пространственное воображение")
    PO = models.IntegerField(verbose_name="Пространственное обобщение")
    PM = models.IntegerField(verbose_name="Память")
    IQ = models.IntegerField(verbose_name="Сводный коэффициент интеллекта")