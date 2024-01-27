# Extrair os IPs do log

import re

data_log = """
Data: 2024-01-26
Horário: 15:32:45
IP de Origem: 192.168.1.100
Página Acessada: /pagina-exemplo

Data: 2024-01-26
Horário: 16:45:22
IP de Origem: 203.120.34.56
Página Acessada: /outra-pagina

Data: 2024-01-26
Horário: 17:58:10
IP de Origem: 72.31.45.98
Página Acessada: /pagina-final
"""

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def extract_ips(text: str):
    ip_occurences = re.findall(ip_pattern, text)
    ips_extracted = ["".join(ip) for ip in ip_occurences]
    return ips_extracted


ips_extracted = extract_ips(data_log)


for index, ip in enumerate(ips_extracted, 1):
    print(f"IP {index}: {ip}")