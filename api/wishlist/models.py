from django.db import models
from api.user.models import CustomUser
from api.course.models import Course

# Create your models here.

class UserWishlist( models.Model ) :
    user = models.ForeignKey( CustomUser , on_delete = models.CASCADE , related_name = 'wishlist' )
    course = models.ForeignKey( Course , on_delete = models.PROTECT , related_name = 'wishlist' )

    def __str__(self) :
        return f'{self.user}-{self.course}'
