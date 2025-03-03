#!/bin/bash

DOMAIN="_acme-challenge.$CERTBOT_DOMAIN"
TOKEN="your-powerdns-api-token"
PDNS_API_URL="https://your-powerdns-api-url/api/v1/servers/localhost/zones/$CERTBOT_DOMAIN."

curl -X PATCH "$PDNS_API_URL" \
    -H "X-API-Key: $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "rrsets": [{
            "name": "'$DOMAIN'",
            "type": "TXT",
            "ttl": 60,
            "changetype": "REPLACE",
            "records": [{
                "content": "\"'$CERTBOT_VALIDATION'\"",
                "disabled": false
            }]
        }]
    }'