import os

from celery import shared_task
import requests

@shared_task
def create_acme_challenge(domain_id):
    from .models import acme_domain
    domain = acme_domain.objects.get(id=domain_id)
    domain_name = domain.domain_name

    # Use Certbot to create ACME challenge
    certbot_command = f"certbot certonly --manual --preferred-challenges dns --manual-auth-hook './scripts/authenticator.sh' -d {domain_name}"
    os.system(certbot_command)

    # Add DNS challenge to PowerDNS
    # You need to implement the authenticator.sh script to handle the DNS challenge with the PowerDNS API

    return f"ACME challenge created for {domain_name}"