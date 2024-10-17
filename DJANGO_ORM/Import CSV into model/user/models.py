from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class ImportedFiles(models.Model):
    title = models.CharField(_('title'), max_length=500)
    authors = models.CharField(_('authors'), max_length=500)
    average_rating = models.FloatField(_('averate_rating'))
    isbn = models.CharField(_('isbn'), max_length=150)
    isbn13 = models.CharField(_('isbn 13'), max_length=150)
    language_code = models.CharField(_('language code'), max_length=10)
    num_pages = models.IntegerField(_('number of pages'))
    ratings_count = models.BigIntegerField(_('rating count'))
    text_reviews_count = models.BigIntegerField(_("text review count"))
    publication_date = models.DateField(_('publication date'), auto_now=True)
    publisher = models.CharField(_("publisher"), max_length=150)
