# Alunos - SIGAA-UFC
Gera automaticamente uma planilha com todos os nomes, matrículas e turmas dos estudantes matriculados em alguma disciplina no SIGAA UFC (Sistema Integrado de Gestão de Atividades Acadêmicas da Universidade Federal do Ceará).

# Requisitos
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/)

# Como usar
**1)** No SIGAA, entre na página da disciplina em que se deseja extrair o nome dos alunos matriculados. Em seguida, no canto esquerdo do site, procure e clique em **Participantes**, como mostrado na figura:

![image](https://user-images.githubusercontent.com/56649205/73856915-f1b5f100-4814-11ea-83e8-73f8d7472ba4.png)

**2)** Na página dos participantes, tem todos os alunos matriculados na disciplina, basta agora salvar esta página em seu computador no local que achar mais conveniente. O nome do arquivo pode ser qualquer um, por exemplo, *sigaa.html*. 

**3)** Após instalado o [python](https://www.python.org/downloads/) no computador e [configurado na linha de comando](http://www.mundodoshackers.com.br/como-executar-um-codigo-python-pelo-prompt-de-comando), basta executar a seguinte linha no prompt de comando:
```
python.exe sigaa.py [NOME DO ARQUIVO].html
```
**OBS**: Tanto o arquivo em python (sigaa.py) quanto a página salva do SIGAA (sigaa.html) devem estar na mesma pasta, como exemplo:

![image](https://user-images.githubusercontent.com/56649205/73859531-f381b380-4818-11ea-8985-d283fc1938ed.png)

**4)** Ao final, será informado o número total de alunos processados e gerado um arquivo (*ListaAlunos.csv*) na mesma pasta o qual poderá ser aberto no Microsoft Excel contendo três colunas: Matrícula, Alunos e Turma. Como mostrado na figura abaixo:

![sigaa-alunos](https://user-images.githubusercontent.com/56649205/73859037-2a0afe80-4818-11ea-8d85-9b59239d7927.jpg)
