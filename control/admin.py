from django.contrib import admin
from control.models import Participant
# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'alt_phone', 'occupation', 'organisation', 'how_know']
	class Meta:
		model = Participant

admin.site.register(Participant, ParticipantAdmin)