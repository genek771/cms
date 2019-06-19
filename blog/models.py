from django.db import models
from django.utils import timezone


class Category(models.Model):
    '''Модель категорий статей'''
    name = models.CharField('Название тега', max_length=150)
    slug = models.SlugField('URL', max_length=160)
    active = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Tag(models.Model):
    '''Модель тегов к статье'''
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('URL', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



class Post(models.Model):
    '''Модель статей'''
    title = models.CharField('Заголовок статьи', max_length=150)
    slug = models.SlugField('URL', max_length=150, null=True)
    sub_title = models.CharField('Подзаголовок', max_length=150)
    mini_text = models.TextField('Превью статьи', max_length=500)
    text = models.TextField('Текст статьи')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    publish_date = models.DateTimeField('Дата публикации', default=timezone.now)
    active = models.BooleanField('Опубликовать', default=True)
    sort = models.PositiveIntegerField('Порядок', default=0, unique=True)
    view = models.PositiveIntegerField('Количество просмотров', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель статьи'
        verbose_name_plural = 'Модели статей'


class Comment(models.Model):
    '''Комментарии'''
    post = models.ForeignKey(Post, verbose_name='Комментарий', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария', max_length=500)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    moderation = models.BooleanField('Модерация', default=False)