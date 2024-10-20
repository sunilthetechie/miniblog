# myapp/views.py

from django.http import HttpResponse
from .models import DummyEntry

def home(request):
    # Create a dummy entry
    DummyEntry.objects.create(name="Dummy Data")

    # Send a response
    return HttpResponse("Dummy entry added to the database!")
