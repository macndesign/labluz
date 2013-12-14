from django.db.models import query


class NoticiaQuerySet(query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)

    def destaques(self):
        return self.filter(destaque=True)
