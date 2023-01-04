from django.contrib import admin
from .models import Player,Session,Attendance,Sport,Transaction,Coach,Renter
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display=['Name','Type','Active']
    list_display_links=['Name','Type']
    list_editable=['Active']
    search_fields=['Name']
    list_filter=['Active','Type','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
class SessionAdmin(admin.ModelAdmin):
    list_display=['Day','Start','End']
    list_display_links=['Start','End']
    list_editable=['Day']
class SportAdmin(admin.ModelAdmin):
    list_display=['SpName','PricMil','PricCivil','MinAge','MaxAge','Forl']
    list_display_links=['Forl']
    list_editable=['SpName','PricMil','PricCivil','MinAge','MaxAge']
class TransactionAdmin(admin.ModelAdmin):
    list_display=['TType','Fees','TDate']
    list_display_links=['TDate']
    list_editable=['TType','Fees']
    search_fields=['TDate']
    list_filter=['TDate','TType']
class CoachAdmin(admin.ModelAdmin):
    list_display=['Name','Sport','CPhone']
    list_display_links=['CPhone']
    list_editable=['Name','Sport']
    search_fields=['Name']
    list_filter=['Sport']
class RenterAdmin(admin.ModelAdmin):
    list_display=['RtName','Location','RDate']
    list_display_links=['RtName','Location']
    list_editable=['RDate']
    search_fields=['Location']
    list_filter=['Location']
admin.site.register(Player,PlayerAdmin)
admin.site.register(Session,SessionAdmin)
#admin.site.register(Attendance)
admin.site.register(Sport,SportAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Coach,CoachAdmin)
admin.site.register(Renter,RenterAdmin)
admin.site.site_header= "Recreation"
admin.site.site_title="Recreation"
