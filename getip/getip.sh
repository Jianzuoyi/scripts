#!/bin/bash

GETIP_DIR=$( cd "$( dirname "$0"  )" && pwd  )
TELECOM="${GETIP_DIR}/telecom.ip"
EDUCATION="${GETIP_DIR}/education.ip"
#DOMAIN_NAME="li059059.xicp.net"
PYTHON=$(which python)
SEND_MAIL="${GETIP_DIR}/send_mail.py"

if [[ ! -f $TELECOM ]]; then
    touch $TELECOM
fi
if [[ ! -f $EDUCATION ]]; then
    touch $EDUCATION
fi

TELECOM_LAST=$(cat $TELECOM)
EDUCATION_LAST=$(cat $EDUCATION)

TELECOM_NOW=$(wget http://members.3322.org/dyndns/getip -O - -q;echo)
#TELECOM_NOW=$(dig $DOMAIN_NAME | grep "^$DOMAIN_NAME" | awk '{print $5}')
EDUCATION_NOW=$(wget http://ipecho.net/plain -O - -q ; echo)

#echo $TELECOM_LAST
#echo $EDUCATION_LAST
#echo $TELECOM_NOW
#echo $EDUCATION_NOW
if [[ $TELECOM_NOW != $TELECOM_LAST ]] || [[ $EDUCATION_NOW != $EDUCATION_LAST ]]; then
   #echo "public ip  changed"
    echo $TELECOM_NOW > $TELECOM
    echo $EDUCATION_NOW > $EDUCATION
    # send email
    $PYTHON $SEND_MAIL $TELECOM $EDUCATION
fi
