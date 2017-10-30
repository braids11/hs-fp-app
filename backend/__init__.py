def process_user_query(query_string):
    names = query_string.split(' ')
    greetings = []
    for i in names:
        greetings.append(f'Hi {i}')
        return greetings

print(process_user_query("Alex Bob"))
