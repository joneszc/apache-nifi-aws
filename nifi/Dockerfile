FROM apache/nifi:1.18.0

ENV NIFI_CONF_PATH $NIFI_HOME/conf

# Switch to root to install the required packages
USER root

RUN yum -y update
RUN yum -y install wget
RUN yum -y install nano
RUN yum -y install python3-pip

##COPY local_requirements.txt .
##RUN ["chmod", "a+x", "local_requirements.txt"]

# install the nar bundles for nifi-atlas hook and dependencies of hive processors
# https://community.cloudera.com/t5/Support-Questions/How-to-report-NiFi-lineage-to-Atlas/m-p/326191
RUN wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-atlas-nar/1.18.0/nifi-atlas-nar-1.18.0.nar -P /opt/nifi/nifi-current/lib \
    && wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-dbcp-service-nar/1.18.0/nifi-dbcp-service-nar-1.18.0.nar -P /opt/nifi/nifi-current/lib \
    && wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-hive-nar/1.18.0/nifi-hive-nar-1.18.0.nar -P /opt/nifi/nifi-current/lib \
    && wget https://repo1.maven.org/maven2/org/apache/nifi/nifi-hive-services-api-nar/1.18.0/nifi-hive-services-api-nar-1.18.0.nar -P /opt/nifi/nifi-current/lib

# add config files for apache-atlas and/or apache-hive integration
ADD conf/atlas-application.properties $NIFI_CONF_PATH
#ADD conf/core-site.xml $NIFI_CONF_PATH
#ADD conf/hive-site.xml $NIFI_CONF_PATH
#ADD conf/hdfs-site.xml $NIFI_CONF_PATH

## Copy config bootstrap file to increase the JVM memory settings
COPY conf/bootstrap.conf $NIFI_CONF_PATH

# enable read/write/exec permissions
# Provide permissions to files nar files
RUN ["chmod", "+x", "/opt/nifi/nifi-current/lib/nifi-dbcp-service-nar-1.18.0.nar"]
RUN ["chmod", "+x", "/opt/nifi/nifi-current/lib/nifi-hive-nar-1.18.0.nar"]
RUN ["chmod", "+x", "/opt/nifi/nifi-current/lib/nifi-hive-services-api-nar-1.18.0.nar"]
RUN ["chmod", "+x", "/opt/nifi/nifi-current/lib/nifi-atlas-nar-1.18.0.nar"]
# Provide permissions to files config files
RUN ["chmod", "+x", "/opt/nifi/nifi-current/conf/atlas-application.properties"]
RUN ["chmod", "+x", "/opt/nifi/nifi-current/conf/bootstrap.conf"]

#RUN rm /etc/pki/ca-trust/source/anchors/ca-bundle.crt

# Switching back to using the `nifi` user
USER nifi

##RUN pip3 install --user -r local_requirements.txt

RUN pip3 install --user pyarrow==2 awswrangler
RUN pip3 install --user --upgrade requests
## Copy over the python scripts
RUN mkdir $NIFI_HOME/python_scripts
COPY --chown=nifi:nifi python_scripts $NIFI_HOME/python_scripts

