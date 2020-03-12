from django.db import models


class Project(models.Model):
  """Portofolio single project"""

  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to="portfolio/images/")
  url = models.URLField(blank=True)

  def __str__(self):
    """Show database item default name in admin section"""

    return self.title