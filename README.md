Ansible IBM MQ Install
==============================

[![Build Status](https://app.travis-ci.com/jpcasas/ibm-mq-ansible-role.svg?branch=master)](https://app.travis-ci.com/jpcasas/ibm-mq-ansible-role)
[![Galaxy](https://img.shields.io/ansible/role/47913)](https://galaxy.ansible.com/jpcasas/ibm_mq_ansible_role)

Tested on:
----------

- CentOS 8
- Ubuntu 18.04

Example
-------

### Install the role:

```bash
ansible-galaxy install jpcasas.ibm_mq_ansible_role

```


### playbook-mq.yml example

```yaml
- name: setup a MQ development environment
  hosts: <host>
  vars:
    mq_qm_name: QM1
    mq_install_dev_objects: yes
    mq_admin_password: password
    mq_enable_webserver: yes
    mq_detect_download_installer: yes # Installs last MQ Advanced Developper from repo IBM
    # mq_local_installer: /vagrant/IBM_MQ_9.1.5_LINUX_X86-64.tar.gz
  roles:
    - jpcasas.ibm_mq_ansible_role
 
```

### Procedure
 - install ansible
 - create a file playbook-mq.yml with the content above 
 - Configure the host example: https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html
 - Run the command 
 ```bash
 ansible-playbook playbook-mq.yml
```

# Installation of MQ with Vagrant
  
  https://github.com/jpcasas/ibm-mq-ansible-example
