FROM apache/nifi-toolkit:1.18.0

# Switch to root to install the required packages
USER root

# Upgrading packages
##Upgrade the Alpine Linux Package Manager itself to the latest available version, before upgrading any other package
RUN apk add --upgrade apk-tools
# Upgrade all installed packages:
RUN apk upgrade --available

COPY scripts/docker-entrypoint.sh /opt/nifi-toolkit/docker-entrypoint.sh
RUN ["chmod", "+x", "/opt/nifi-toolkit/docker-entrypoint.sh"]

ENTRYPOINT ["/opt/nifi-toolkit/docker-entrypoint.sh"]