#! python3
# coding: latin-1

from bs4 import BeautifulSoup
import re,sys
import pandas as pd

nomes=['Alunos']
matricula=['Matrícula']
turma=['Turma']
combinacao=[]

# Get HTML
soup = BeautifulSoup(open(sys.argv[1]), "html.parser")
alunos_table = soup.findAll("table", {"class" : "participantes"})[1]

# Get students information
for i in alunos_table.findAll("td", {"valign" : "top"}):
    nomes.append(i.find('strong').text.strip().title())
    matricula.append(''.join(re.findall(r'Matrícula: <em>(\d+)', str(i))))
    turma.append(''.join(re.findall(r'Turma: <em>(\d*\w*)', str(i))))
    
# CSV File
for i in range(0,len(nomes)):
    combinacao=[matricula[i],nomes[i],turma[i]]
    df=pd.DataFrame(combinacao)
    with open('ListaAlunos.csv', 'a', encoding='utf-16', newline='') as f:
        df.transpose().to_csv(f, encoding='iso-8859-1', header=False, sep = "\t", index=False)

print("Arquivo Criado com Sucesso !")
print(str(len(nomes)-1) + ' alunos matriculados.')