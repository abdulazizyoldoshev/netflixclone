from django.db import IntegrityError

from django.db import models
from django.utils.translation import gettext_lazy as _
from detailed_movies.models import *
from django.utils.html import mark_safe
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50, verbose_name=_('category name'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class TagModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class MoviesModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'), null=True, blank=True)
    year = models.DateTimeField(verbose_name=_('year'), null=True, blank=True)
    ratingMovie = models.CharField(max_length=10, verbose_name=_('rating of Movie'))
    duration = models.CharField(max_length=10, verbose_name=_('duration'))
    presented_description = models.TextField(verbose_name=_('presented description'), null=True, blank=True)
    detailed_description = models.TextField(verbose_name=_('detailed description'), null=True, blank=True)
    film = models.FileField(upload_to='media/videos/', verbose_name=_('film'), null=True, blank=True)
    poster_img = models.ImageField(upload_to='media/posters/&Y/%m/%d/', verbose_name=_('Poster of movies'),
                                   null=True, blank=True)
    logo_img = models.ImageField(upload_to='media/logos/', verbose_name=_('Logo of Movie'),
                                 null=True, blank=True)
    tv_show = models.BooleanField(default=False, verbose_name=_('tv show'))
    tag = models.ManyToManyField(TagModel,
                                 related_name='movies',
                                 verbose_name=_('tags'))
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='movies',
                                 verbose_name=_('category'),
                                 )
    director = models.ManyToManyField(DirectorModel,
                                      related_name='movies',
                                      verbose_name=_('director')
                                      )
    screenplay = models.ManyToManyField(ScreenPlayModel,
                                        related_name='movies',
                                        verbose_name=_('screenplay')
                                        )
    producer = models.ManyToManyField(ProducerModel,
                                      related_name='movies',
                                      verbose_name=_('producer')
                                      )
    award = models.ManyToManyField(AwardsModel,
                                   related_name='movies',
                                   verbose_name=_('award')
                                   )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return str(self.name)

    @property
    def thumbnail_preview(self):
        if self.poster_img:
            return mark_safe('<img src="{}" width="230" height="150" />'.format(self.poster_img.url))
        return ""

    @property
    def thumbnail_preview_film(self):
        if self.film:
            return mark_safe('<img src="{}" width="230" height="150" />'.format(self.film.url))
        return ""

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')


#
class MyList(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name=_('mylist')
    )
    movie = models.ForeignKey(
        MoviesModel,
        on_delete=models.CASCADE,
        verbose_name=_('movie'),
        related_name=_('mylist')
    )

    # def __str__(self):
    #     return self.user.username() + ' | ' + self.movie.name

    @staticmethod
    def add_and_delete(user, movie):
        try:
            MyList.objects.create(user=user, movie=movie)
        except IntegrityError:
            MyList.objects.all().filter(user=user, movie=movie).delete()

    class Meta:
        verbose_name = _('mylist')
        verbose_name_plural = _('mylists')
        unique_together = 'user', 'movie',

