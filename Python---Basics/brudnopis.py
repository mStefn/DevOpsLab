---
- name: Webserver setup
  hosts: webservers
  become: yes
  tasks:
    - name: Install httpd
      ansible.builtin.yum:
        name: httpd
        state: present

- name: DBserver setup
  hosts: dbservers
  become: yes
  tasks:
    - name: Install mariadb-server
      ansible.builtin.yum:
        name: mariadb-server
        state: present
