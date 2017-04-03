from django.db import models
from django.utils import timezone

# class(객체)의 이름을 정의할 때, 첫글자 항상 대문자여야함는
# models.Model => Post가 장고 모델임을 의미. 이 코드로 인해 장고는 Post가 데이터베이스에 저장되어야된다고 알게됨.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title