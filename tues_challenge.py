---
- name: Tuesday Challenge
  hosts: planet express
  connection: network_cli
  gather_facts: yes

  tasks:
   - name: print out the variable named "result"
     debug:
       var: result
       
   -apt:
       name: sl
       state: present
   name: using apt to install sl
   register: result
