with open(r'systeminfocomponents.txt', 'r', encoding='utf-8') as input_file:
    query_string = input_file.read()
    d = {}
    current_year = 2017
    blocks = query_string.split('\n\n')
    for block in blocks:
        device = ''
        driver = ''
        for line in block.splitlines():
            if line.startswith('Name	'):
                device = line.split('\t')[1]
                print(device)
            if line.startswith('Driver	') and device != '':
                driver = line.split(' ')[-2]
#                    year = int(driver.split('/')[-1] + driver.split('/')[-2])
                year = int(driver.split('/')[-1])
        if device != '' and driver != '':
                d[device]=year
    for device, driver in d.items():
        delta = current_year - driver
        if delta >= 1:
            d[device] = 'Upgrade Now!'
        elif delta <= 0:
            d[device] = 'Up-To-Date'
    return(d)

print(process_user_query("hello"))
