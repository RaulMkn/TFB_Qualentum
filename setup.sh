#!/bin/bash

source .env

echo "[INFO] Descargando jenkins-cli.jar desde $JENKINS_URL"
curl -O "$JENKINS_URL/jnlpJars/jenkins-cli.jar"

echo "[INFO] Creando job en Jenkins..."
java -jar jenkins-cli.jar -s "$JENKINS_URL" -auth "$JENKINS_USER:$JENKINS_TOKEN" create-job "$JENKINS_JOB_NAME" < job.xml

echo "[INFO] Job creado correctamente."
