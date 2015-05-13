# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin
from PIL import Image
from cStringIO import StringIO
from . import config

DEF_SIZE = (800, 600)
DEF_EXTENSION = 'jpeg'
        

class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    interval = models.IntegerField(default=5000)
    
    def copy_relations(self, oldinstance):
        for item in oldinstance.carouselitem_set.all():
            item.pk = None
            item.carousel = self
            item.save()
    
    def __unicode__(self):
        return self.domid


class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel, verbose_name=_("Carousel"))
    caption_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Caption Title"))
    button_title = models.CharField(max_length=255, blank=True, verbose_name=_("Button Title"))
    button_url = models.URLField(blank=True, verbose_name=_("Button URL"))
    caption_content = models.TextField(blank=True, null=True, verbose_name=_("Caption Content"))
    image = models.ImageField(upload_to=getattr(settings, "CAROUSEL_UPLOADS_FOLDER", "uploads/"),
                              blank=True, null=True, verbose_name=_("Image"))
    text_position = models.CharField(max_length=10, choices=config.CAROUSEL_TEXT_POSITIONS,
                                     default=config.CAROUSEL_TEXT_POSITION_LEFT, verbose_name=_("Text Position"))
    transition = models.CharField(max_length=30, choices=config.CAROUSEL_TRANSITION_CHOICES,
                                  default=config.CAROUSEL_TRANS_NO_TRANSITION, verbose_name=_("Transition"))
    start_position = models.CharField(max_length=20, choices=config.CAROUSEL_MOVEMENT_POSITION_CHOICES,
                                      default=config.CAROUSEL_MOVEMENT_POSITION_LEFT_TOP_LABEL,
                                      verbose_name=_("Start Position"))
    end_position = models.CharField(max_length=20, choices=config.CAROUSEL_MOVEMENT_POSITION_CHOICES,
                                    default=config.CAROUSEL_MOVEMENT_POSITION_LEFT_TOP_LABEL,
                                    verbose_name=_("End Position"))

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image.file)
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            size = getattr(settings, "BOOTSTRAP_CAROUSEL_IMGSIZE", DEF_SIZE)
            extension = getattr(settings, "BOOTSTRAP_CAROUSEL_FILE_EXTENSION", DEF_EXTENSION)
            if size != img.size:
                img.thumbnail(size, Image.ANTIALIAS)

                temp_handle = StringIO()
                img.save(temp_handle, extension)
                temp_handle.seek(0)

                suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                         temp_handle.read(), content_type='image/%s' % extension)
                fname = "%s.%s" % (os.path.splitext(self.image.name)[0], extension)
                self.image.save(fname, suf, save=False)

        super(CarouselItem, self).save()
