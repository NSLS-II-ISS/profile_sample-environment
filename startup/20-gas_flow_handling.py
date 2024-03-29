
gases_flow_dict = {
            'He': {'ch1': {
                        'mfc':ghs_ch1_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                   'ch2': {
                        'mfc': ghs_ch2_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    # 'inert': {
                    #     'mfc': mfc_cart_inert,
                    #     'selector': None,
                    #     'manifold': None,
                    #     'valves': []},
                    'full_gas_name': 'Helium',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'Ar': {'ch1': {
                        'mfc':ghs_ch1_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc1_sp,
                        'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    'full_gas_name': 'Argon',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'N2': {'ch1': {
                       'mfc':ghs_ch1_mfc1_sp,
                       'selector': ghs_mnf1_gas_selector,
                        'manifold': '1',
                        'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream]},
                   'ch2': {
                       'mfc': ghs_ch2_mfc1_sp,
                       'selector': ghs_mnf1_gas_selector,
                       'manifold': '1',
                       'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream]},
                    'full_gas_name': 'Nitrogen',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'O2': {'ch1': {
                        'mfc': ghs_ch1_mfc6_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf6_upstream, ghs_mnf6_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc6_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf6_upstream, ghs_mnf6_ch2_dnstream]},
                    'full_gas_name': 'Oxygen',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'CO2': {'ch1': {
                        'mfc': ghs_ch1_mfc8_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf8_upstream, ghs_mnf8_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc8_sp,
                        'selector': None,
                        'manifold': None,
                        'valves': [ghs_mnf8_upstream, ghs_mnf8_ch2_dnstream]},
                    'full_gas_name': 'Carbon Dioxide',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'C2H4': {'ch1': {
                        'mfc': ghs_ch1_mfc3_sp,
                        'selector': ghs_mnf3_gas_selector,
                        'manifold': '3',
                        'valves': [ghs_mnf3_upstream, ghs_mnf3_ch1_dnstream]},
                    'ch2': {
                        'mfc': ghs_ch2_mfc3_sp,
                        'selector': ghs_mnf3_gas_selector,
                        'manifold': '3',
                        'valves': [ghs_mnf3_upstream, ghs_mnf3_ch2_dnstream]},
                    'full_gas_name': 'Ethylene',
                    # 'group_switch_valve': switch_manifold['ghs'],
                    'group': 'ghs'},
            'CH4': {'gas_cart': {
                        'mfc': mfc_cart_1,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_ch4]},
                    'full_gas_name': 'Methane',
                    # 'group_switch_valve': switch_manifold['cart'],
                    'group': 'cart'},
            'CO': {'gas_cart': {
                       'mfc': mfc_cart_2,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_co]},
                    'full_gas_name': 'Carbon Monoxide',
                    # 'group_switch_valve': switch_manifold['cart'],
                    'group': 'cart'},
            'H2': {'gas_cart': {
                        'mfc': mfc_cart_3,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_h2]},
                    'full_gas_name': 'Hydrogen',
                    'group': 'cart'},
            # 'He': {},
            #        'ch2': {
            #        'mfc': mfc_cart_inert,
            #        'selector': None,
            #        'manifold': None,
            #        'valves': []},
            #        'full_gas_name': 'Helium',
            #        'group': 'inert',
            #        'group_switch_valve': switch_manifold['inert']},
    }

def flow(gas, source='GHS Ch1', flow_rate=0):
    if source == 'GHS Ch1':
        _source = 'ch1'
    elif source == 'GHS Ch2':
        _source = 'ch2'
    elif source == 'Gas cart':
        _source = 'gas_cart'
    # elif source == 'Inert':
    #     _source = 'inert'

    # open or close valves
    for valve in gases_flow_dict[gas][_source]['valves']:
        if flow_rate > 0:
             valve.put(1)
        else:
            valve.put(0)

    if gases_flow_dict[gas][_source]['manifold']:
        indx_mnf = gases_flow_dict[gas][_source]['manifold']
        gas_command = ghs['manifolds'][indx_mnf]['gases'][gases_flow_dict[gas]['full_gas_name']]
        ghs['manifolds'][indx_mnf]['gas_selector'].put(gas_command)

    gases_flow_dict[gas][_source]['mfc'].put(flow_rate)


def handle_switching_valve(switch_valve_dict):
    switch_valve_status_dict = {k: 0 for k in switch_manifold.keys()}

    # if switch_valve_dict['GHS Ch1'] == 'exhaust':
    #     ghs['channels']['1']['exhaust'].put(1)
    #     ghs['channels']['1']['reactor'].put(0)
    # else:
    #     ghs['channels']['1']['reactor'].put(1)
    #     ghs['channels']['1']['exhaust'].put(0)
    #     switch_valve_status_dict['ghs'] = 1
    #
    # if switch_valve_dict['GHS Ch2'] == 'exhaust':
    #     ghs['channels']['2']['exhaust'].put(1)
    #     ghs['channels']['2']['reactor'].put(0)
    # else:
    #     ghs['channels']['2']['reactor'].put(1)
    #     ghs['channels']['2']['exhaust'].put(0)
    #     switch_valve_status_dict['ghs'] = 1

    if switch_valve_dict['GHS Ch1'] == 'reactor':
        switch_valve_status_dict['ghs_ch1'] = 1

    if switch_valve_dict['GHS Ch2'] == 'reactor':
        switch_valve_status_dict['ghs_ch2'] = 1

    if switch_valve_dict['Gas cart'] == 'reactor':
        switch_valve_status_dict['cart'] = 1

    for valve_key, valve_status in switch_valve_status_dict.items():
        switch_manifold[valve_key].put(valve_status)

