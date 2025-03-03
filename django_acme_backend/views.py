from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import acme_domain
from .tasks import create_acme_challenge

@login_required
def create_challenge(request, domain_id):
    create_acme_challenge.delay(domain_id)
    return HttpResponse("ACME challenge creation started.")

@login_required
def list_domains(request):
    domains = acme_domain.objects.all()
    return render(request, 'list_domains.html', {'domains': domains})