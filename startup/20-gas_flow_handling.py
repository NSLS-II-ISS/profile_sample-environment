
gases_flow_dict = {
        # 'He': {'ch1': {
        #                 'mfc':ghs_ch1_mfc1_sp,
        #                 'selector': ghs_mnf1_gas_selector,
        #                 'manifold':'1',
        #                 'valves': [ghs_mnf1_upstream, ghs_mnf1_ch1_dnstream, switch_manifold['ghs']]},
        #             'ch2': {
        #                 'mfc': ghs_ch2_mfc1_sp,
        #                 'selector': ghs_mnf1_gas_selector,
        #                 'manifold': '1',
        #                 'valves': [ghs_mnf1_upstream, ghs_mnf1_ch2_dnstream, switch_manifold['ghs']]},
        #             'full_gas_name': 'Helium'},
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
                    'group': 'ghs',
                    'group_switch_valve': switch_manifold['ghs']},
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
                    'group': 'ghs',
                    'group_switch_valve': switch_manifold['ghs']},
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
                    'group': 'ghs',
                    'group_switch_valve': switch_manifold['ghs']},
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
                    'group': 'ghs',
                    'group_switch_valve': switch_manifold['ghs']},
            'CH4': {'ch1': {
                        'mfc': mfc_cart_1,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_ch4]},
                    'ch2': {
                        'mfc': mfc_cart_1,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_ch4]},
                    'full_gas_name': 'Methane',
                    'group': 'cart',
                    'group_switch_valve': switch_manifold['cart']},
            'CO': {'ch1': {
                       'mfc': mfc_cart_2,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_co]},
                    'ch2': {
                        'mfc': mfc_cart_2,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_co]},
                    'full_gas_name': 'Carbon Monoxide',
                    'group': 'cart',
                    'group_switch_valve': switch_manifold['cart']},
            'H2': {'ch1': {
                        'mfc': mfc_cart_3,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_h2]},
                    'ch2': {
                        'mfc': mfc_cart_3,
                        'selector': None,
                        'manifold': None,
                        'valves': [valve_h2]},
                    'full_gas_name': 'Hydrogen',
                    'group': 'cart'},
            'He': {'ch1': {
                        'mfc': mfc_cart_inert,
                        'selector': None,
                        'manifold': None,
                        'valves': []},
                   'ch2': {
                   'mfc': mfc_cart_inert,
                   'selector': None,
                   'manifold': None,
                   'valves': []},
                   'full_gas_name': 'Helium',
                   'group': 'inert',
                   'group_switch_valve': switch_manifold['inert']},
    }

def flow(gas, channel=0, flow_rate=0):
    if channel == 1:
        ch_name = 'ch1'
    else:
        ch_name = 'ch2'

    # open or close valves
    for valve in gases_flow_dict[gas][ch_name]['valves']:
        if flow_rate > 0:
             # valve.set(1)
             valve.put(1)
        else:
            # valve.set(0)
            valve.put(0)
    if gases_flow_dict[gas][ch_name]['manifold']:
        indx_mnf = gases_flow_dict[gas][ch_name]['manifold']
        gas_command = ghs['manifolds'][indx_mnf]['gases_flow_dict'][gases_flow_dict[gas]['full_gas_name']]
        # print(f'Gas command {gas_command}')
        # ghs['manifolds'][indx_mnf]['gas_selector'].set(gas_command)
        ghs['manifolds'][indx_mnf]['gas_selector'].put(gas_command)

    # gases_flow_dict[gas][ch_name]['mfc'].set(flow_rate)
    gases_flow_dict[gas][ch_name]['mfc'].put(flow_rate)


def handle_switching_valve(flow_gas_dict):
    switch_valve_status_dict = {k: 0 for k in switch_manifold.keys()}
    for gas, flowrate in flow_gas_dict.items():
        if flowrate > 0:
            group = gases_flow_dict[gas]['group']
            switch_valve_status_dict[group] = 1

    for valve_key, valve_status in switch_valve_status_dict.items():
        switch_manifold[valve_key].put(valve_status)

