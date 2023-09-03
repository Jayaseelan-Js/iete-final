from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_date = models.DateField()
    doi = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    

    def __str__(self):
        return self.title
    
class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.title
    
class Research(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField()
    genere = models.TextField(max_length=50)
    image = models.ImageField(upload_to='research_images/', blank=True, null=True)
   

    def __str__(self):
        return self.title
    

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_date = models.DateField(auto_now_add=True)
    salary = models.TextField(max_length=20)
    job_type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
def gallery_image_upload_to(instance, filename):
    return f'gallery/{instance.title}/{filename}'

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=gallery_image_upload_to)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    gallerty_type = models.TextField(max_length=20, default='default')

    def __str__(self):
        return self.title


