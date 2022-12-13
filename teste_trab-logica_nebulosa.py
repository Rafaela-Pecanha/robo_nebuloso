import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import requests
from tkinter import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions

#Febrícula:  37,3℃ a 37,8℃; Febre: Acima de 37,8℃;  Febre alta:  a partir de 39℃
febre = ctrl.Antecedent(np.arange(36.1, 42.1, 0.1), 'febre')
dificuldade_de_respirar = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'dificuldade_de_respirar')
tosse = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'tosse')

# OUTPUT
grau = ctrl.Consequent(np.arange(0, 4.1, 0.1), 'grau')

#membership function
febre['sem_febre'] = fuzz.trimf(febre.universe, [36.1, 36.1, 37.3])
febre['febricula'] = fuzz.trimf(febre.universe, [37.0, 37.3, 38])
febre['febre'] = fuzz.trimf(febre.universe, [37.8, 38.5, 39])
febre['febre_alta'] = fuzz.trapmf(febre.universe, [38.5, 39.5, 42, 43])

dificuldade_de_respirar['baixa'] = fuzz.trapmf(dificuldade_de_respirar.universe, [0, 0, 2, 4])
dificuldade_de_respirar['media'] = fuzz.trapmf(dificuldade_de_respirar.universe, [2, 4, 6, 8])
dificuldade_de_respirar['alta'] = fuzz.trapmf(dificuldade_de_respirar.universe, [6, 8, 10, 10])

tosse['baixa'] = fuzz.trapmf(tosse.universe, [0, 0, 2, 4])
tosse['media'] = fuzz.trapmf(tosse.universe, [2, 4, 6, 8])
tosse['alta'] = fuzz.trapmf(tosse.universe, [6, 8, 10, 10])


grau['assintomatico'] = fuzz.trapmf(grau.universe, [0, 0, 1, 1.5])
grau['sintomatico'] = fuzz.trapmf(grau.universe, [1, 1.5,2.5, 3])
grau['grave'] = fuzz.trapmf(grau.universe, [2.5, 3, 4, 4])


# You can see how these look with .view()
rule1 = ctrl.Rule(dificuldade_de_respirar['alta'], grau['grave'])
rule2 = ctrl.Rule(dificuldade_de_respirar['media'] & (febre['febre_alta'] | tosse['alta']), grau['grave'])
rule3 = ctrl.Rule(dificuldade_de_respirar['media'] & (febre['febre_alta'] | tosse['alta']), grau['grave'])
rule4 = ctrl.Rule(dificuldade_de_respirar['media'] & febre['febre'] & tosse['media'], grau['grave'])
rule5 = ctrl.Rule(febre['febre_alta'] & (tosse['alta'] | tosse['media']), grau['grave'])

rule6 = ctrl.Rule(dificuldade_de_respirar['media'] & tosse['baixa'] & febre['febricula'], grau['sintomatico'])
rule7 = ctrl.Rule(dificuldade_de_respirar['media'] & tosse['media'] & febre['febricula'], grau['sintomatico'])
rule8 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['alta'] & febre['febricula'], grau['sintomatico'])
rule9 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['baixa'] & febre['febre_alta'], grau['sintomatico'])
rule10 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['baixa'] & febre['febre'], grau['sintomatico'])
rule11 = ctrl.Rule(dificuldade_de_respirar['media'] & tosse['baixa'] & febre['febre'], grau['sintomatico'])
rule12 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['media'] & febre['febre'], grau['sintomatico'])
rule13 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['alta'] & febre['febre'], grau['sintomatico'])
rule14 = ctrl.Rule(dificuldade_de_respirar['media'] & tosse['baixa'] & febre['sem_febre'], grau['sintomatico'])
rule15 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['alta'] & febre['sem_febre'], grau['sintomatico'])


rule16 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['baixa'] & febre['febricula'], grau['assintomatico'])
rule17 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['media'] & febre['febricula'], grau['assintomatico'])
rule18 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['media'] & febre['sem_febre'], grau['assintomatico'])
rule19 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['baixa'] & febre['febricula'], grau['assintomatico'])
rule20 = ctrl.Rule(dificuldade_de_respirar['baixa'] & tosse['baixa'] & febre['sem_febre'], grau['assintomatico'])


avaliacao_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
                                rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, 
                                rule17, rule18, rule19, rule20])
avaliacao = ctrl.ControlSystemSimulation(avaliacao_ctrl)


class Application:
    def __init__(self, master=None):
        root.title("Sintoma Covid-19")

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["padx"] = 20
        self.container1["pady"] = 5
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        
        self.lblidusuario = Label(self.container1,
        text="Digite a febre do paciente em Cº:", font=self.fonte)
        self.lblidusuario.pack(side=LEFT)

        self.txtfebre = Entry(self.container1)
        self.txtfebre["width"] = 10
        self.txtfebre["font"] = self.fonte
        self.txtfebre.pack(side=LEFT)
       

        self.lblrespirar = Label(self.container2,
        text="Digite a dificuldade de respirar do paciente (0-10):", font=self.fonte)
        self.lblrespirar.pack(side=LEFT)
        
        self.txtrespirar = Entry(self.container2)
        self.txtrespirar["width"] = 10
        self.txtrespirar["font"] = self.fonte
        self.txtrespirar.pack(side=LEFT)
        

        self.lbltosse = Label(self.container3,
        text="Digite o nível de tosse do paciente (0-10):", font=self.fonte)
        self.lbltosse.pack(side=LEFT)

        self.txttosse = Entry(self.container3)
        self.txttosse["width"] = 10
        self.txttosse["font"] = self.fonte
        self.txttosse.pack(side=LEFT)
                
    
        self.botao1 = Button(root, text="envia", command=enviar)
        self.botao1.pack()


def enviar():
    avaliacao.input['dificuldade_de_respirar'] =  float(app.txtrespirar.get())
    avaliacao.input['tosse'] = float(app.txttosse.get())
    avaliacao.input['febre'] = float(app.txtfebre.get())
    avaliacao.compute()
    grau.view(sim=avaliacao)

root = Tk()
app = Application(root)
root.mainloop()

