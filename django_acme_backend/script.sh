#!/bin/sh

#POWERDNS_API_URL="http://pdns:8081/api/v1/servers/localhost/zones"
#POWERDNS_API_KEY="your-powerdns-api-token"

DOMAIN=$CERTBOT_DOMAIN

curl -X PATCH "${POWERDNS_API_URL}/${DOMAIN}." \
    -H "X-API-Key: ${POWERDNS_API_KEY}" \
    -H "Content-Type: application/json" \
    --data '{
      "rrsets": [{
        "name": "_acme-challenge.'"${DOMAIN}"'.",
        "type": "TXT",
        "ttl": 60,
        "changetype": "REPLACE",
        "records": [{
          "content": "\"'"${CERTBOT_VALIDATION}"'\""
        }]
      }]
    }' > /dev/null

echo "Updated DNS record for ${DOMAIN} with token ${CERTBOT_VALIDATION}"
sleep 25