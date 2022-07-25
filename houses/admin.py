from django.contrib import admin
from .models import Amenity,Agent,House,Image_of_house,Blog,Comment,Message,AgentAccount
# Register your models here.
admin.site.register(Amenity)
admin.site.register(Agent)
admin.site.register(House)
admin.site.register(Image_of_house)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(AgentAccount)