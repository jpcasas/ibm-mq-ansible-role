Ansible IBM MQ Install
==============================

Tested on:
----------

- CentOS 8
- Ubuntu 18.04

Example
-------

### Install the role:

```bash
ansible-galaxy 

```


### playbook.yml example

```yaml
- name: setup a MQ development environment
  hosts: centos
  vars:
   - ibm_mq:
       qm_name: QM
       install_install_dev_objects: yes
       mq_admin_password: password
       enable_webserver: yes
       download_installer: yes
       auto_detect_install: yes
  roles:
    - jpc.ibm-mq-ansible-role

```

