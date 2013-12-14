# coding: utf-8
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from labluz.core.managers import NoticiaManager, AtivoManager


class FotoNoticia(models.Model):
    foto = models.ImageField(u'Foto da notícia', upload_to='noticia')
    noticia = models.ForeignKey('Noticia', related_name='fotos')
    legenda = models.CharField(u'Legenda', max_length=120, blank=True)
    texto = models.TextField('Texto', blank=True)

    def __unicode__(self):
        return self.foto.name


class Noticia(models.Model):
    autor = models.CharField(u'Autor', max_length=120, blank=True)
    titulo = models.CharField(u'Título', max_length=120)
    slug = models.SlugField(max_length=120)
    data_pub = models.DateTimeField(u'Data de publicação', auto_now_add=True)
    subtitulo = models.CharField(u'Subtítulo', max_length=120, blank=True)
    texto = models.TextField('Texto', blank=True)
    fonte = models.CharField(u'Link da fonte', max_length=120, blank=True)
    foto_principal = models.ImageField('Foto principal', upload_to='noticia', blank=True)
    video = models.TextField(u'Vídeo', blank=True)
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)

    # Audit
    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=False
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=False
    )

    # Manager
    objects = NoticiaManager()
    ativos = AtivoManager()

    class Meta:
        verbose_name = u'Notícia'
        ordering = ['-data_pub']

    @models.permalink
    def get_absolute_url(self):
        return ('core:noticia', None, {
            'year': str(self.data_pub.year),
            'month': str(self.data_pub.month).zfill(2),
            'day': str(self.data_pub.day).zfill(2),
            'slug': str(self.slug),
        })

    def __unicode__(self):
        return self.titulo


@receiver(pre_save, sender=Noticia)
def save_slug_noticia(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(sender.titulo)
