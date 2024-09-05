#afs mount: Define this SID
sap_id = 'rh6'
hdbadm_uid = 'testing'
platform = 'SYSBASE'
sidadm_uid = 'testing2'
asesidadm_uid = 'testing3'
scs_instance_number = '1'
pas_instance_number = '2'
app_instance_number = '3'
list_of_servers = ['SCS','DB']
first_server_temp = []

def setting_vars():
    this_sid = {
        'sid': sap_id.upper(),
        'dbsid_uid': hdbadm_uid,
        'sidadm_uid': asesidadm_uid if platform == 'SYSBASE' else sidadm_uid,
        'ascs_inst_no': scs_instance_number,
        'pas_inst_no': pas_instance_number,
        'app_inst_no': app_instance_number 
    }
    all_sap_mounts = {'testing4': 'testing5'}
    try: 
        all_sap_mounts =  multi_sids 
    except:
        all_sap_mounts = dict(**all_sap_mounts, **this_sid)

    for server in list_of_servers:
        first_server = query(sap_id.upper()+'_'+server)
        first_server_temp.append(first_server)

    afs_mnt_options = 'noresvport,vers=4,minorversion=1,sec=sys'
    mnt_options = {
        'afs_mnt_options': 'noresvport,vers=4,minorversion=1,sec=sys',
        'anf_mnt_options': 'rw,nfsvers=4.1,hard,timeo=600,rsize=262144,wsize=262144,noatime,lock,_netdev,sec=sys'
    }

    print(this_sid)
    print(all_sap_mounts)
    print(first_server_temp)
    return this_sid, all_sap_mounts, first_server_temp, mnt_options

def query(full_hostname):
    with open('/etc/ansible/hosts', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if full_hostname in line: 
                return full_hostname

if __name__ == "__main__":
    this_sid, all_sap_mounts, first_server_temp, mnt_options = setting_vars()

