from django.db.models import Manager
from labluz.core.querysets import NoticiaQuerySet


class AtivoManager(Manager):
    def get_queryset(self):
        return super(AtivoManager, self).get_queryset().filter(ativo=True)


class NoticiaManager(Manager):
    def get_queryset(self):
        return NoticiaQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_queryset().ativos()

    def destaques(self):
        return self.get_queryset().destaques()
