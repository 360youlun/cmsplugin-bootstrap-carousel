# coding=utf-8
"""
Configurations about Carousel Items.
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Carousel item position configures
CAROUSEL_TEXT_POSITION_LEFT = 'left'
CAROUSEL_TEXT_POSITION_CENTER = 'center'
CAROUSEL_TEXT_POSITION_RIGHT = 'right'

CAROUSEL_TEXT_POSITION_LEFT_LABEL = _('Left')
CAROUSEL_TEXT_POSITION_CENTER_LABEL = _('Center')
CAROUSEL_TEXT_POSITION_RIGHT_LABEL = _('Right')

CAROUSEL_TEXT_POSITIONS = getattr(
    settings,
    'CAROUSEL_TEXT_POSITIONS',
    ((CAROUSEL_TEXT_POSITION_LEFT, CAROUSEL_TEXT_POSITION_LEFT_LABEL),
     (CAROUSEL_TEXT_POSITION_CENTER, CAROUSEL_TEXT_POSITION_CENTER_LABEL),
     (CAROUSEL_TEXT_POSITION_RIGHT, CAROUSEL_TEXT_POSITION_RIGHT_LABEL))
)

#Carousel item transition configures
CAROUSEL_TRANS_BOX_SLIDE = 'boxslide'
CAROUSEL_TRANS_BOX_FADE = 'boxfade'
CAROUSEL_TRANS_SLOT_SLIDE_HORIZONTAL = 'slotslide-horizontal'
CAROUSEL_TRANS_SLOT_SLIDE_VERTICAL = 'slotslide-vertical'
CAROUSEL_TRANS_CURTAIN_1 = 'curtain-1'
CAROUSEL_TRANS_CURTAIN_2 = 'curtain-2'
CAROUSEL_TRANS_CURTAIN_3 = 'curtain-3'
CAROUSEL_TRANS_SLOT_ZOOM_HORIZONTAL = 'slotzoom-horizontal'
CAROUSEL_TRANS_SLOT_ZOOM_VERTICAL = 'slotzoom-vertical'
CAROUSEL_TRANS_SLOT_FADE_HORIZONTAL = 'slotfade-horizontal'
CAROUSEL_TRANS_SLOT_FADE_VERTICAL = 'slotfade-vertical'
CAROUSEL_TRANS_FADE = 'fade'
CAROUSEL_TRANS_SLIDE_LEFT = 'slideleft'
CAROUSEL_TRANS_SLIDE_UP = 'slideup'
CAROUSEL_TRANS_SLIDE_DOWN = 'slidedown'
CAROUSEL_TRANS_SLIDE_RIGHT = 'slideright'
CAROUSEL_TRANS_PAPER_CUT = 'papercut'
CAROUSEL_TRANS_3D_CURTAIN_HORIZONTAL = '3dcurtain-horizontal'
CAROUSEL_TRANS_3D_CURTAIN_VERTICAL = '3dcurtain-vertical'
CAROUSEL_TRANS_CUBIC = 'cubic'
CAROUSEL_TRANS_CUBE = 'cube'
CAROUSEL_TRANS_FLY_IN = 'flyin'
CAROUSEL_TRANS_TURN_OFF = 'turnoff'
CAROUSEL_TRANS_IN_CUBE = 'incube'
CAROUSEL_TRANS_CUBIC_HORIZONTAL = 'cubic-horizontal'
CAROUSEL_TRANS_CUBE_HORIZONTAL = 'cube-horizontal'
CAROUSEL_TRANS_IN_CUBE_HORIZONTAL = 'incube-horizontal'
CAROUSEL_TRANS_TURN_OFF_VERTICAL = 'turnoff-vertical'
CAROUSEL_TRANS_FADE_FROM_RIGHT = 'fadefromright'
CAROUSEL_TRANS_FADE_FROM_LEFT = 'fadefromleft'
CAROUSEL_TRANS_FADE_FROM_TOP = 'fadefromtop'
CAROUSEL_TRANS_FADE_FROM_BOTTOM = 'fadefrombottom'
CAROUSEL_TRANS_FADE_TO_LEFT_FADE_FROM_RIGHT = 'fadetoleftfadefromright'
CAROUSEL_TRANS_FADE_TO_RIGHT_FADE_TO_LEFT = 'fadetorightfadetoleft'
CAROUSEL_TRANS_FADE_TO_BOTTOM_FADE_FROM_TOP = 'fadetobottomfadefromtop'
CAROUSEL_TRANS_FADE_TO_TOP_FADE_FROM_BOTTOM = 'fadetotopfadefrombottom'
CAROUSEL_TRANS_PARALLAX_TO_RIGHT = 'parallaxtoright'
CAROUSEL_TRANS_PARALLAX_TO_LEFT = 'parallaxtoleft'
CAROUSEL_TRANS_PARALLAX_TO_TOP = 'parallaxtotop'
CAROUSEL_TRANS_PARALLAX_TO_BOTTOM = 'parallaxtobottom'
CAROUSEL_TRANS_SCALE_DOWN_FROM_RIGHT = 'scaledownfromright'
CAROUSEL_TRANS_SCALE_DOWN_FROM_LEFT = 'scaledownfromleft'
CAROUSEL_TRANS_SCALE_DOWN_FROM_TOP = 'scaledownfromtop'
CAROUSEL_TRANS_SCALE_DOWN_FORM_BOTTOM = 'scaledownfrombottom'
CAROUSEL_TRANS_ZOOM_OUT = 'zoomout'
CAROUSEL_TRANS_ZOOM_IN = 'zoomin'
CAROUSEL_TRANS_NO_TRANSITION = 'notransition'

CAROUSEL_TRANS_BOX_SLIDE_LABEL = _('Box Slide')
CAROUSEL_TRANS_BOX_FADE_LABEL = _('Box Fade')
CAROUSEL_TRANS_SLOT_SLIDE_HORIZONTAL_LABEL = _('Slot Slide Horizontal')
CAROUSEL_TRANS_SLOT_SLIDE_VERTICAL_LABEL = _('Slot Slide Vertical')
CAROUSEL_TRANS_CURTAIN_1_LABEL = _('Curtain 1')
CAROUSEL_TRANS_CURTAIN_2_LABEL = _('Curtain 2')
CAROUSEL_TRANS_CURTAIN_3_LABEL = _('Curtain 3')
CAROUSEL_TRANS_SLOT_ZOOM_HORIZONTAL_LABEL = _('Slot Zoom Horizontal')
CAROUSEL_TRANS_SLOT_ZOOM_VERTICAL_LABEL = _('Slot Zoom Vertical')
CAROUSEL_TRANS_SLOT_FADE_HORIZONTAL_LABEL = _('Slot Fade Horizontal')
CAROUSEL_TRANS_SLOT_FADE_VERTICAL_LABEL = _('Slot Fade Vertical')
CAROUSEL_TRANS_FADE_LABEL = _('Fade')
CAROUSEL_TRANS_SLIDE_LEFT_LABEL = _('Slide Left')
CAROUSEL_TRANS_SLIDE_UP_LABEL = _('Slide Up')
CAROUSEL_TRANS_SLIDE_DOWN_LABEL = _('Slide Down')
CAROUSEL_TRANS_SLIDE_RIGHT_LABEL = _('Slide Right')
CAROUSEL_TRANS_PAPER_CUT_LABEL = _('Paper Cut')
CAROUSEL_TRANS_3D_CURTAIN_HORIZONTAL_LABEL = _('3d Curtain Horizontal')
CAROUSEL_TRANS_3D_CURTAIN_VERTICAL_LABEL = _('3d Curtain Vertical')
CAROUSEL_TRANS_CUBIC_LABEL = _('Cubic')
CAROUSEL_TRANS_CUBE_LABEL = _('Cube')
CAROUSEL_TRANS_FLY_IN_LABEL = _('Fly in')
CAROUSEL_TRANS_TURN_OFF_LABEL = _('Turn off')
CAROUSEL_TRANS_IN_CUBE_LABEL = _('In Cube')
CAROUSEL_TRANS_CUBIC_HORIZONTAL_LABEL = _('Cubic Horizontal')
CAROUSEL_TRANS_CUBE_HORIZONTAL_LABEL = _('Cube Horizontal')
CAROUSEL_TRANS_IN_CUBE_HORIZONTAL_LABEL = _('In Cube Horizontal')
CAROUSEL_TRANS_TURN_OFF_VERTICAL_LABEL = _('Turn off Vertical')
CAROUSEL_TRANS_FADE_FROM_RIGHT_LABEL = _('Fade from Right')
CAROUSEL_TRANS_FADE_FROM_LEFT_LABEL = _('Fade from Left')
CAROUSEL_TRANS_FADE_FROM_TOP_LABEL = _('Fade from Top')
CAROUSEL_TRANS_FADE_FROM_BOTTOM_LABEL = _('Fade from Bottom')
CAROUSEL_TRANS_FADE_TO_LEFT_FADE_FROM_RIGHT_LABEL = _('Fade to Left Fade from Right')
CAROUSEL_TRANS_FADE_TO_RIGHT_FADE_TO_LEFT_LABEL = _('Fade to Right Fade to Left')
CAROUSEL_TRANS_FADE_TO_BOTTOM_FADE_FROM_TOP_LABEL = _('Fade to Bottom Fade from Top')
CAROUSEL_TRANS_FADE_TO_TOP_FADE_FROM_BOTTOM_LABEL = _('Fade to Top Fade from Bottom')
CAROUSEL_TRANS_PARALLAX_TO_RIGHT_LABEL = _('Parallax to Right')
CAROUSEL_TRANS_PARALLAX_TO_LEFT_LABEL = _('Parallax to Left')
CAROUSEL_TRANS_PARALLAX_TO_TOP_LABEL = _('Parallax to Top')
CAROUSEL_TRANS_PARALLAX_TO_BOTTOM_LABEL = _('Parallax to Bottom')
CAROUSEL_TRANS_SCALE_DOWN_FROM_RIGHT_LABEL = _('Scale Down from Right')
CAROUSEL_TRANS_SCALE_DOWN_FROM_LEFT_LABEL = _('Scale Down from Left')
CAROUSEL_TRANS_SCALE_DOWN_FROM_TOP_LABEL = _('Scale Down from Top')
CAROUSEL_TRANS_SCALE_DOWN_FORM_BOTTOM_LABEL = _('Scale Down from Bottom')
CAROUSEL_TRANS_ZOOM_OUT_LABEL = _('Zoom out')
CAROUSEL_TRANS_ZOOM_IN_LABEL = _('Zoom in')
CAROUSEL_TRANS_NO_TRANSITION_LABEL = _('No Transition')

CAROUSEL_TRANSITION_CHOICES = getattr(
    settings,
    'CAROUSEL_TRANSITION_CHOICES',
    ((CAROUSEL_TRANS_BOX_SLIDE, CAROUSEL_TRANS_BOX_SLIDE_LABEL),
     (CAROUSEL_TRANS_BOX_FADE, CAROUSEL_TRANS_BOX_FADE_LABEL),
     (CAROUSEL_TRANS_SLOT_SLIDE_HORIZONTAL, CAROUSEL_TRANS_SLOT_SLIDE_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_SLOT_SLIDE_VERTICAL, CAROUSEL_TRANS_SLOT_SLIDE_VERTICAL_LABEL),
     (CAROUSEL_TRANS_CURTAIN_1, CAROUSEL_TRANS_CURTAIN_1_LABEL),
     (CAROUSEL_TRANS_CURTAIN_2, CAROUSEL_TRANS_CURTAIN_2_LABEL),
     (CAROUSEL_TRANS_CURTAIN_3, CAROUSEL_TRANS_CURTAIN_3_LABEL),
     (CAROUSEL_TRANS_SLOT_ZOOM_HORIZONTAL, CAROUSEL_TRANS_SLOT_ZOOM_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_SLOT_ZOOM_VERTICAL, CAROUSEL_TRANS_SLOT_ZOOM_VERTICAL_LABEL),
     (CAROUSEL_TRANS_SLOT_FADE_HORIZONTAL, CAROUSEL_TRANS_SLOT_FADE_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_SLOT_FADE_VERTICAL, CAROUSEL_TRANS_SLOT_FADE_VERTICAL_LABEL),
     (CAROUSEL_TRANS_FADE, CAROUSEL_TRANS_FADE_LABEL),
     (CAROUSEL_TRANS_SLIDE_LEFT, CAROUSEL_TRANS_SLIDE_LEFT_LABEL),
     (CAROUSEL_TRANS_SLIDE_UP, CAROUSEL_TRANS_SLIDE_UP_LABEL),
     (CAROUSEL_TRANS_SLIDE_DOWN, CAROUSEL_TRANS_SLIDE_DOWN_LABEL),
     (CAROUSEL_TRANS_SLIDE_RIGHT, CAROUSEL_TRANS_SLIDE_RIGHT_LABEL),
     (CAROUSEL_TRANS_PAPER_CUT, CAROUSEL_TRANS_PAPER_CUT_LABEL),
     (CAROUSEL_TRANS_3D_CURTAIN_HORIZONTAL, CAROUSEL_TRANS_3D_CURTAIN_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_3D_CURTAIN_VERTICAL, CAROUSEL_TRANS_3D_CURTAIN_VERTICAL_LABEL),
     (CAROUSEL_TRANS_CUBIC, CAROUSEL_TRANS_CUBIC_LABEL),
     (CAROUSEL_TRANS_CUBE, CAROUSEL_TRANS_CUBE_LABEL),
     (CAROUSEL_TRANS_FLY_IN, CAROUSEL_TRANS_FLY_IN_LABEL),
     (CAROUSEL_TRANS_TURN_OFF, CAROUSEL_TRANS_TURN_OFF_LABEL),
     (CAROUSEL_TRANS_IN_CUBE, CAROUSEL_TRANS_IN_CUBE_LABEL),
     (CAROUSEL_TRANS_CUBIC_HORIZONTAL, CAROUSEL_TRANS_CUBIC_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_CUBE_HORIZONTAL, CAROUSEL_TRANS_CUBE_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_IN_CUBE_HORIZONTAL, CAROUSEL_TRANS_IN_CUBE_HORIZONTAL_LABEL),
     (CAROUSEL_TRANS_TURN_OFF_VERTICAL, CAROUSEL_TRANS_TURN_OFF_VERTICAL_LABEL),
     (CAROUSEL_TRANS_FADE_FROM_RIGHT, CAROUSEL_TRANS_FADE_FROM_RIGHT_LABEL),
     (CAROUSEL_TRANS_FADE_FROM_LEFT, CAROUSEL_TRANS_FADE_FROM_LEFT_LABEL),
     (CAROUSEL_TRANS_FADE_FROM_TOP, CAROUSEL_TRANS_FADE_FROM_TOP_LABEL),
     (CAROUSEL_TRANS_FADE_FROM_BOTTOM, CAROUSEL_TRANS_FADE_FROM_BOTTOM_LABEL),
     (CAROUSEL_TRANS_FADE_TO_LEFT_FADE_FROM_RIGHT, CAROUSEL_TRANS_FADE_TO_LEFT_FADE_FROM_RIGHT_LABEL),
     (CAROUSEL_TRANS_FADE_TO_RIGHT_FADE_TO_LEFT, CAROUSEL_TRANS_FADE_TO_RIGHT_FADE_TO_LEFT_LABEL),
     (CAROUSEL_TRANS_FADE_TO_BOTTOM_FADE_FROM_TOP, CAROUSEL_TRANS_FADE_TO_BOTTOM_FADE_FROM_TOP_LABEL),
     (CAROUSEL_TRANS_FADE_TO_TOP_FADE_FROM_BOTTOM, CAROUSEL_TRANS_FADE_TO_TOP_FADE_FROM_BOTTOM_LABEL),
     (CAROUSEL_TRANS_PARALLAX_TO_RIGHT, CAROUSEL_TRANS_PARALLAX_TO_RIGHT_LABEL),
     (CAROUSEL_TRANS_PARALLAX_TO_LEFT, CAROUSEL_TRANS_PARALLAX_TO_LEFT_LABEL),
     (CAROUSEL_TRANS_PARALLAX_TO_TOP, CAROUSEL_TRANS_PARALLAX_TO_TOP_LABEL),
     (CAROUSEL_TRANS_PARALLAX_TO_BOTTOM, CAROUSEL_TRANS_PARALLAX_TO_BOTTOM_LABEL),
     (CAROUSEL_TRANS_SCALE_DOWN_FROM_RIGHT, CAROUSEL_TRANS_SCALE_DOWN_FROM_RIGHT_LABEL),
     (CAROUSEL_TRANS_SCALE_DOWN_FROM_LEFT, CAROUSEL_TRANS_SCALE_DOWN_FROM_LEFT_LABEL),
     (CAROUSEL_TRANS_SCALE_DOWN_FROM_TOP, CAROUSEL_TRANS_SCALE_DOWN_FROM_TOP_LABEL),
     (CAROUSEL_TRANS_SCALE_DOWN_FORM_BOTTOM, CAROUSEL_TRANS_SCALE_DOWN_FORM_BOTTOM_LABEL),
     (CAROUSEL_TRANS_ZOOM_OUT, CAROUSEL_TRANS_ZOOM_OUT_LABEL),
     (CAROUSEL_TRANS_ZOOM_IN, CAROUSEL_TRANS_ZOOM_IN_LABEL),
     (CAROUSEL_TRANS_NO_TRANSITION, CAROUSEL_TRANS_NO_TRANSITION_LABEL))
)

CAROUSEL_MOVEMENT_POSITION_LEFT_TOP = "left top"
CAROUSEL_MOVEMENT_POSITION_CENTER_TOP = "center top"
CAROUSEL_MOVEMENT_POSITION_RIGHT_TOP = "right top"
CAROUSEL_MOVEMENT_POSITION_LEFT_CENTER = "left center"
CAROUSEL_MOVEMENT_POSITION_CENTER_CENTER = "center center"
CAROUSEL_MOVEMENT_POSITION_RIGHT_CENTER = "right center"
CAROUSEL_MOVEMENT_POSITION_LEFT_BOTTOM = "left bottom"
CAROUSEL_MOVEMENT_POSITION_CENTER_BOTTOM = "center bottom"
CAROUSEL_MOVEMENT_POSITION_RIGHT_BOTTOM = "right bottom"

CAROUSEL_MOVEMENT_POSITION_LEFT_TOP_LABEL = _("Left Top")
CAROUSEL_MOVEMENT_POSITION_CENTER_TOP_LABEL = _("Center Top")
CAROUSEL_MOVEMENT_POSITION_RIGHT_TOP_LABEL = _("Right Top")
CAROUSEL_MOVEMENT_POSITION_LEFT_CENTER_LABEL = _("Left Center")
CAROUSEL_MOVEMENT_POSITION_CENTER_CENTER_LABEL = _("Center Center")
CAROUSEL_MOVEMENT_POSITION_RIGHT_CENTER_LABEL = _("Right Center")
CAROUSEL_MOVEMENT_POSITION_LEFT_BOTTOM_LABEL = _("Left Bottom")
CAROUSEL_MOVEMENT_POSITION_CENTER_BOTTOM_LABEL = _("Center Bottom")
CAROUSEL_MOVEMENT_POSITION_RIGHT_BOTTOM_LABEL = _("Right Bottom")

CAROUSEL_MOVEMENT_POSITION_CHOICES = getattr(
    settings,
    'CAROUSEL_MOVEMENT_POSITION_CHOICES',
    ((CAROUSEL_MOVEMENT_POSITION_LEFT_TOP, CAROUSEL_MOVEMENT_POSITION_LEFT_TOP_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_CENTER_TOP, CAROUSEL_MOVEMENT_POSITION_CENTER_TOP_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_RIGHT_TOP, CAROUSEL_MOVEMENT_POSITION_RIGHT_TOP_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_LEFT_CENTER, CAROUSEL_MOVEMENT_POSITION_LEFT_CENTER_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_CENTER_CENTER, CAROUSEL_MOVEMENT_POSITION_CENTER_CENTER_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_RIGHT_CENTER, CAROUSEL_MOVEMENT_POSITION_RIGHT_CENTER_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_LEFT_BOTTOM, CAROUSEL_MOVEMENT_POSITION_LEFT_BOTTOM_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_CENTER_BOTTOM, CAROUSEL_MOVEMENT_POSITION_CENTER_BOTTOM_LABEL),
     (CAROUSEL_MOVEMENT_POSITION_RIGHT_BOTTOM, CAROUSEL_MOVEMENT_POSITION_RIGHT_BOTTOM_LABEL))
)
