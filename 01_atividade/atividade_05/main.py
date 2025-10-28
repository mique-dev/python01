# declaracao de lista
nomes = ["Acre (AC)","Amapá (AP)","Amazonas (AM)","Pará (PA)","Rondônia (RO)","Roraima (RR)","Tocantins (TO)","Alagoas (AL)","Bahia (BA)","Ceará (CE)","Maranhão (MA)","Paraíba (PB)","Pernambuco (PE)","Piauí (PI)","Rio Grande do Norte (RN)","Sergipe (SE)","Região Centro-Oeste:","Distrito Federal (DF)","Goiás (GO)","Mato Grosso (MT)","Mato Grosso do Sul (MS)","Região Sudeste:","Espírito Santo (ES)","Minas Gerais (MG)","Rio de Janeiro (RJ)","São Paulo (SP)","Região Sul:","Paraná (PR)","Rio Grande do Sul (RS)","Santa Catarina (SC)"]

# comnados extras
import os
import time

# exibir lista em ordem alfabetica
nomes.sort()

# re-exibir lista em ordem alfabetica
os.system("cls")

print("\nOrdem alfabética: \n")
for nome in nomes:
    print(nome)
    time.sleep(1)
    os.system("cls")

# exibi a lista completa

print("\nOrdem alfabética: \n")
for nome in nomes:
    print(nome)