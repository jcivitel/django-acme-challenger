from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .tasks import create_acme_challenge


@login_required
def create_challenge(request, domain_id):
    create_acme_challenge.delay(domain_id)
    messages.success(request, f"ACME challenge created successfully for domain ID {domain_id}.")
    return HttpResponseRedirect(reverse('dashboard'))
