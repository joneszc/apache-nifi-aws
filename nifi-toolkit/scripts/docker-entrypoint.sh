#!/bin/bash

/opt/nifi-toolkit/*/bin/tls-toolkit.sh standalone -o /opt/certs -n nifi[0-2].mxs -P ${TRUSTSTORE_PASSWORD} -K ${KEYSTORE_PASSWORD} -S ${KEYSTORE_PASSWORD}; chown -R nifi:nifi /opt/certs
