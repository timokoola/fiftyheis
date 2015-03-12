#!/usr/bin/python
# -*- coding: utf-8 -*-
from twython import TwythonStreamer
from twython import Twython
from twython.exceptions import TwythonError
import re
import pprint
import time
import json
import random
r = random.Random()
import datetime

heis = ["moi", "moikka", "mitäs", "terve", "terppa", "morienttes", "mitämitä", "tsaukki", "mitä äijä", "heippa", "hellurei", "hei sun heiluvilles", "moro", "poro", "päivää", "päevää", "morjens", "tervis", "terskamaheppi", "termos", "heissan", "morjestarallaa", "terve mieheen", "moikku", "hola", "heissuli", "jassoo", "hejdå", "vieläk sääki elät", "helou", "tervehdys", "terve vaan terve", "tsau", "kuisso", "moikkandeeros", "heip", "moikkanen", "komiaa", "moro nääs", "muija", "tähän käteen", "terveisii", "ehtoota talohon", "hai sie", "huomentapäivää", "tseenare", "aloha", "tere", "jumalan terve", "heipparallaa"]

keyfile = "test.keys"
me = "fiftyheis"
api = None

def ilta_aamu():
	now = datetime.datetime.now().hour
	if now < 12:
		return " Ja mahtavan hyvää huomenta!"
	else:
		return " Ja oikein mainiota iltaa!"


def random_terve():
	text = r.choice(heis) 
	result = text[0].upper() + text[1:] + "!" + ilta_aamu()
	return result

class TwythonHelper:

    def __init__(self, keyfile):
        f = open(keyfile)
        lines = f.readlines()
        f.close()
        self.consumerkey = lines[0].split("#")[0]
        self.consumersecret = lines[1].split("#")[0]
        self.accesstoken = lines[2].split("#")[0]
        self.accesssec = lines[3].split("#")[0]

        self.api = Twython(self.consumerkey, self.consumersecret, self.accesstoken, self.accesssec)

if __name__ == '__main__':
    helper = (TwythonHelper(keyfile))
    api = helper.api
    api.update_status(status=random_terve())