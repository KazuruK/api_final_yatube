from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='Уникальный идентификатор группы')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')


class Post(models.Model):
    group = models.ForeignKey(Group, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='group_posts',
                              verbose_name='Группа')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        """
        Overriding base __str__. Outputs the name of the group.
        """
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following',
            )
        ]

    def clean(self):
        if self.user == self.following:
            raise ValidationError('Нельзя подписаться на самого себя')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super(Follow, self).save()
