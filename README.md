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
  hosts: <host>
  vars:
    mq_qm_name: QM1
    mq_install_dev_objects: yes
    mq_admin_password: password
    mq_enable_webserver: yes
    mq_detect_download_installer: yes # Installs last MQ Advanced Developper from repo IBM
    # mq_download_installer: yes # Installs version 9.1.5 MQ Advanced Developper
    # mq_local_installer: /vagrant/IBM_MQ_9.1.5_LINUX_X86-64.tar.gz
  roles:
    - jpc.ibm-mq-ansible-role

```

