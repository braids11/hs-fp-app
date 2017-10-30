#def process_user_query(query_string):
#    names = query_string.split()
#    greetings = []
#    for i in names:
#        greetings.append(f'Hi {i}')
#    return greetings

# print(process_user_query("Alex Bob Mike"))

def process_user_query(query_string):
    names = query_string.split()
    greetings = []
    for i in names:
        if i.istitle():
            greetings.append(f'Hi {i}!')
    greetings = set(greetings)
    return greetings

#print(process_user_query("Alex Alex went to Mike dinner with Animesh"))
