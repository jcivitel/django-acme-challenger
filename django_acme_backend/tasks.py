import subprocess

import requests

from django_acme_challenger.celery import app


@app.task
def create_acme_challenge(domain_id):
    from .models import acme_domain
    domain = acme_domain.objects.get(id=domain_id)
    domain_name = domain.domain_name

    check_if_zone_exists(domain_name)
    certbot_command = f"certbot certonly -v --manual --preferred-challenges dns -d {domain_name}"
    return subprocess.call(certbot_command, shell=True)


def check_if_zone_exists(domain_name):
    api_url = "http://localhost:8081/api/v1/servers/localhost/zones"
    headers = {
        "X-API-Key": "your-powerdns-api-token",
        "Content-Type": "application/json"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        zones = response.json()
        for zone in zones:
            if zone['name'] == domain_name + '.':
                return True
        response = requests.post(api_url, headers=headers, json={"name": domain_name + ".", "kind": "Native"})
        if response.status_code == 201:
            print(f"Zone {domain_name} created successfully.")
            return True
        else:
            print(f"Failed to create zone {domain_name}.")
            return False
