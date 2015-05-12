# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_bootstrap_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='end_position',
            field=models.CharField(default='Left Top', max_length=20, choices=[(b'left top', 'Left Top'), (b'center top', 'Center Top'), (b'right top', 'Right Top'), (b'left center', 'Left Center'), (b'center center', 'Center Center'), (b'right center', 'Right Center'), (b'left bottom', 'Left Bottom'), (b'center bottom', 'Center Bottom'), (b'right bottom', 'Right Bottom')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='start_position',
            field=models.CharField(default='Left Top', max_length=20, choices=[(b'left top', 'Left Top'), (b'center top', 'Center Top'), (b'right top', 'Right Top'), (b'left center', 'Left Center'), (b'center center', 'Center Center'), (b'right center', 'Right Center'), (b'left bottom', 'Left Bottom'), (b'center bottom', 'Center Bottom'), (b'right bottom', 'Right Bottom')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='text_position',
            field=models.CharField(default=b'left', max_length=10, choices=[(b'left', 'Left'), (b'center', 'Center'), (b'right', 'Right')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='transition',
            field=models.CharField(default=b'notransition', max_length=30, choices=[(b'boxslide', 'Box Slide'), (b'boxfade', 'Box Fade'), (b'slotslide-horizontal', 'Slot Slide Horizontal'), (b'slotslide-vertical', 'Slot Slide Vertical'), (b'curtain-1', 'Curtain 1'), (b'curtain-2', 'Curtain 2'), (b'curtain-3', 'Curtain 3'), (b'slotzoom-horizontal', 'Slot Zoom Horizontal'), (b'slotzoom-vertical', 'Slot Zoom Vertical'), (b'slotfade-horizontal', 'Slot Fade Horizontal'), (b'slotfade-vertical', 'Slot Fade Vertical'), (b'fade', 'Fade'), (b'slideleft', 'Slide Left'), (b'slideup', 'Slide Up'), (b'slidedown', 'Slide Down'), (b'slideright', 'Slide Right'), (b'papercut', 'Paper Cut'), (b'3dcurtain-horizontal', '3d Curtain Horizontal'), (b'3dcurtain-vertical', '3d Curtain Vertical'), (b'cubic', 'Cubic'), (b'cube', 'Cube'), (b'flyin', 'Fly in'), (b'turnoff', 'Turn off'), (b'incube', 'In Cube'), (b'cubic-horizontal', 'Cubic Horizontal'), (b'cube-horizontal', 'Cube Horizontal'), (b'incube-horizontal', 'In Cube Horizontal'), (b'turnoff-vertical', 'Turn off Vertical'), (b'fadefromright', 'Fade from Right'), (b'fadefromleft', 'Fade from Left'), (b'fadefromtop', 'Fade from Top'), (b'fadefrombottom', 'Fade from Bottom'), (b'fadetoleftfadefromright', 'Fade to Left Fade from Right'), (b'fadetorightfadetoleft', 'Fade to Right Fade to Left'), (b'fadetobottomfadefromtop', 'Fade to Bottom Fade from Top'), (b'fadetotopfadefrombottom', 'Fade to Top Fade from Bottom'), (b'parallaxtoright', 'Parallax to Right'), (b'parallaxtoleft', 'Parallax to Left'), (b'parallaxtotop', 'Parallax to Top'), (b'parallaxtobottom', 'Parallax to Bottom'), (b'scaledownfromright', 'Scale Down from Right'), (b'scaledownfromleft', 'Scale Down from Left'), (b'scaledownfromtop', 'Scale Down from Top'), (b'scaledownfrombottom', 'Scale Down from Bottom'), (b'zoomout', 'Zoom out'), (b'zoomin', 'Zoom in'), (b'notransition', 'No Transition')]),
            preserve_default=True,
        ),
    ]
