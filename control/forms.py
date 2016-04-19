from django.forms import ModelForm
from control.models import Participant
from django.core.exceptions import NON_FIELD_ERRORS


class ParticipantForm(ModelForm):
    class Meta:
		model = Participant
		fields = ['name', 'email', 'phone', 'alt_phone', 'occupation', 'organisation', 'how_know']