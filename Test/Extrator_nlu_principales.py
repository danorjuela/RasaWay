from rasa_nlu.training_data import load_data
from rasa_nlu import config
import sys
import json
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def run_nlu():
	f = open('./Resultado/ciudadesResultadoPrincipales.txt', 'w')
	interpreter = Interpreter.load('../src/models/nlu/default/nlu')
	with open("./Data/ciudadesPrincipales.txt", "r") as r:
		ciudades = r.readlines()
	for ciudad in ciudades:
		city = ciudad.rstrip('\n')
		data = interpreter.parse("en " + city)
		try:
			if data["entities"][0]["value"].lower() != city.lower():
				print (data["entities"][0]["value"] +" " + city)
				f.write("- ["+ city+"](location)\n")
		except:
				pass
				
if __name__ == '__main__':
	run_nlu()
