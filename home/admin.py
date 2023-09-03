from django.contrib import admin
from .models import News, Publication, Events, Education, Research, Job, GalleryImage, Images

# Register your models here.

admin.site.register(News)
admin.site.register(Publication)
admin.site.register(Events)
admin.site.register(Education)
admin.site.register(Research)
admin.site.register(Job)
admin.site.register(GalleryImage)
admin.site.register(Images)