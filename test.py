def run_module():
    sap_sid = 'rh6'
    hdbadm_uid = 'testing'
    platform = 'SYSBASE'
    sidadm_uid = 'testing2'
    asesidadm_uid = 'testing3'
    scs_instance_number = '1'
    pas_instance_number = '2'
    app_instance_number = '3'

    result = {
        "this_sid": {},
        "all_sap_mounts": [],
        "first_server_temp": [],
        "mnt_options": {}
    }

    result['this_sid'] = {
    'sid': sap_sid.upper(),
    'dbsid_uid': hdbadm_uid,
    'sidadm_uid': asesidadm_uid if platform == 'SYSBASE' else sidadm_uid,
    'ascs_inst_no': scs_instance_number,
    'pas_inst_no': pas_instance_number,
    'app_inst_no': app_instance_number 
}

    try:
        if 'multi_sids' in locals():
            result['all_sap_mounts'] = multi_sids
        else:
#            result['all_sap_mounts'] = result['all_sap_mounts'] + result['this_sid']
            print("testing")
            result['all_sap_mounts'].append(result['this_sid'])

    except Exception as e:
        print(e)
    return result

if __name__ == "__main__":
    result=run_module()
    print(result)
