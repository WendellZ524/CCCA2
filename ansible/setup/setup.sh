#!/bin/bash

. ./unimelb-comp90024-2021-grp-21-openrc.sh; ansible-playbook -i ./inventory/hosts.ini setup.yaml