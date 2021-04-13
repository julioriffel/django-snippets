from django.db.models.query import QuerySet


class PostQuerySet(QuerySet):
    def public_posts(self):
        return self.filter(public=True)


PostManager = PostQuerySet.as_manager
