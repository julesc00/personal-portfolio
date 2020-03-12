from django.db import models

class Post(models.Model):
  """Create Post model"""

  title = models.CharField(max_length=100)
  date_created = models.DateTimeField(auto_now_add=True)
  post_body = models.TextField()
  url = models.URLField(blank=True)

  def __str__(self):
    """Show database item default name in admin section"""

    return self.title



