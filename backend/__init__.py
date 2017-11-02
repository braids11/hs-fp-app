def process_user_query(query_string):
    #with open(r'systeminfocomponents.txt', 'r', encoding='utf-8') as input_file:
        #query_string = input_file.read()
    d = {}
    current_year = 2017
    blocks = query_string.split('\n\n')
    for block in blocks:
        device = ''
        driver = ''
        for line in block.splitlines():
            if line.startswith('Name	'):
                device = line.split('\t')[1]
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

#print(process_user_query("hello"))


#
#
#
#         print(lists)
#         for string in lists:
#             if string.startswith('Name	')
#                 print(string)
#             if string.startswith('Driver	'):
#                 driver_dates.append(string.split(' ')[-2])
#
#     print(driver_dates)
#         for i in driver_dates:
#
#     print(drivers)
#
#     dict = {}
#     driver_dates = []
#
#
#     return result
#
#
#     for line in input_file:
#
#
# string = 'Driver	c:\windows\system32\drivers\i8042prt.sys (10.0.14393.0, 111.50 KB (114,176 bytes), 16/07/2016 12:41)'
# date_1 = string.split(' ')
# print(date_1)
# date_2 = []
# >>> x = "fffagggahhh"
# >>> k = x.split('a')
# >>> j = [k[0]] + ['a'+l for l in k[1:]]
# >>> j
# ['fff', 'aggg', 'ahhh']
#
#
#
#
#
#
#
#
#             if string.startswith('Driver	') or string.startswith('Name	'):
#                 if 'Audio' in string:
# #                drivers.append(string)
#                     print(string)
#             #if string.startswith('Name	'):
#             #    print(string)
# #               names.append(string.split('] '))
#
# #            elif string.startswith('Name	Driver	Port Name	Server Name'):
# #                continue
# #            elif string.startswith('Name	'):
# #                names.append(string.split('	'))
# #for i in names:
# #    del i[0]
# print(drivers)
#
#
#
#     for
#         for i in names:
#             del i[0]
#
#         print(f'{names}')
#
# f'{name}'
#         print(x)
#         if x.startswith('Name'):
#             names = f'{name}'
#         elif x.startswith('Driver'):
#             drivers = f'{drivers}'
#
# print(names)
#
#
#
# #rint(process_user_query("Alex Alex went to Mike dinner with Animesh"))
# #comment
#
# #with open(r'students.csv', 'r', encoding='utf-8') as input_file:
# #    for x in input_file:
# #        x = x.strip()
# #        print(x.split(';'))
