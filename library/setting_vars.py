from ansible.module_utils.basic import AnsibleModule
#afs mount: Define this SID
#sap_id = 'rh6'
#hdbadm_uid = 'testing'
#platform = 'SYSBASE'
#sidadm_uid = 'testing2'
#asesidadm_uid = 'testing3'
#scs_instance_number = '1'
#pas_instance_number = '2'
#app_instance_number = '3'
#list_of_servers = ['SCS','DB']
first_server_temp = []

def run_module():
    module_args = dict(
        sap_id=dict(type="str", required=True),
        hdbadm_uid=dict(type="str", required=True),
        platform=dict(type="str", required=True),
        sidadm_uid=dict(type="str", required=True),
        multi_sids=dict(type='list', required=False),
        asesidadm_uid=dict(type="str", required=False),
        scs_instance_number=dict(type="str", required=True),
        pas_instance_number=dict(type="str", required=True),
        app_instance_number=dict(type="str", required=True),
        list_of_servers=dict(type="list", required=True),
    )

    result = {
        "this_sid": {},
        "all_sap_mounts": {},
        "first_server_temp": [],
        "mnt_options": {}
    }
    
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    result['this_sid'] = {
        'sid': sap_id.upper(),
        'dbsid_uid': hdbadm_uid,
        'sidadm_uid': asesidadm_uid if platform == 'SYSBASE' else sidadm_uid,
        'ascs_inst_no': scs_instance_number,
        'pas_inst_no': pas_instance_number,
        'app_inst_no': app_instance_number 
    }
    try: 
        result['all_sap_mounts'] =  multi_sids 
    except:
        result['all_sap_mounts'] = dict(**all_sap_mounts, **this_sid)

    for server in list_of_servers:
        first_server = query(sap_id.upper()+'_'+server)
        result['first_server_temp'].append(first_server)

    #afs_mnt_options = 'noresvport,vers=4,minorversion=1,sec=sys'
    result['mnt_options'] = {
        'afs_mnt_options': 'noresvport,vers=4,minorversion=1,sec=sys',
        'anf_mnt_options': 'rw,nfsvers=4.1,hard,timeo=600,rsize=262144,wsize=262144,noatime,lock,_netdev,sec=sys'
    }

    print(this_sid)
    print(all_sap_mounts)
    print(first_server_temp)
  
    module.exit_json(**result)

def query(full_hostname):
    with open('/etc/ansible/hosts', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if full_hostname in line: 
                return full_hostname

if __name__ == "__main__":
    run_module()

