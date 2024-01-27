import re

data_log = """
Nome: João Silva
Email: joao.silva@email.com
Telefone: (123) 456-7890

Nome: Maria Oliveira
Email: maria.oliveira@email.com
Telefone: (987) 654-3210

Nome: Carlos Santos
Email: carlos.santos@email.com
Telefone: (555) 123-4567
"""

extract_data_pattern = r"Nome: (.*)\nEmail: (.*)\nTelefone: (.*)"

def extract_user_data(data):
    return {
        "name": data[0],
        "email": data[1],
        "phone": data[2]
    }

def extract_users():
    data_found = re.findall(extract_data_pattern, data_log)
    users = list(map(extract_user_data, data_found))
    return users

user_list = extract_users()
print(user_list)
