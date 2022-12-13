# 1.Motivação
Trabalho da disciplina de lógica nebulosa, no qual era necessário a implementação do modelo fuzzy, sendo assim foi desenvolvido o modelo para o auxílio da avaliação dos sintomas da Covid-19. Visto que, a Covid-19 possui sintomas muito parecidos com os sintomas da gripe, dificultando ainda mais no diagnóstico precoce, além do mais ocorre de alguns pacientes infectados desenvolverem de forma assintomática a doença, o que acaba contribuindo para o aumento da disseminação da doença. Dessa forma,  tendo em vista os sintomas da Covid-19 conhecidos até o momento: febre, falta de ar, tosse, espirros, dores no corpo, mal estar, coriza ou nariz entupidos, dor na garganta, diarreia, dor de cabeça, cansaço, perda do olfato ou paladar; a proposta do robô nebuloso foi utilizar apenas 3 sintomas, no qual a partir das intensidade de cada um  deles o  paciente poderia ser classificado como assintomático, sintomático ou grave, levando em consideração que o paciente já efetuou o teste de Covid-19 e testou positivo. Tal sistema  seria para auxiliar o médico na definição da categoria a qual o paciente pertence, tendo em vista que a categorização certa contribui para a não sobrecarga de leitos, gastos desnecessários dos recursos escassos e aplicação do tratamento adequado.

# 2.Tecnologias utilizadas

O modelo fuzzy foi desenvolvido do zero utilizando a linguagem de programação Python 3 e as bibliotecas ‘scikit-fuzzy’ (versão 0.4.2) para os processos de construção de função de pertencimento (membership function), tanto das variáveis de entrada como a das variáveis de saída, bem como também a construção das regras e a eventual defuzzificação. Também foi utilizada a biblioteca padrão do Python 3 ‘tkinter’ para a construção de uma interface gráfica simples.


## 2.1 Passo a Passo 
Para rodar o arquivo test_trab-logica-nebulosa, será necessário possuir o python instalado na sua máquina, caso não tenha faça o donwolad através [deste link](https://www.python.org/downloads/). Depois será necessário criar um ambiente virtual em seu repositório, para isso é só digitar o comando  `python -m venv venv` no terminal. Após isso, será necessário acessar o ambiente virtual por meio do comando `venv\Scripts\activate`, com isso intala-se o django pelo comando `pip install django`.
Para intalar a bibliotecas ‘scikit-fuzzy’ rode no terminal o comando `pip install -U scikit-fuzzy`, para a biblioteca matplotlib o comando `python -m pip install -U matplotlib`, e por fim para interface gráfica da biblioteca Tkinter o comando `pip install tk`.


## GitHub dos Membros

Luca Machado Mendonça:
Rafaela Peçanha Mathias Fernandaes: https://github.com/Rafaela-Pecanha
