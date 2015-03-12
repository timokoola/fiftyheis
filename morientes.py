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

heis = ["moi", "moikka", "mitäs", "terve", "terppa", "morienttes", "mitämitä", "tsaukki", "mitä äijä", "heippa", "hellurei", "hei sun heiluvilles", "moro", "poro", "päivää", "päevää", "morjens", "tervis", "terskamaheppi", "termos", "heissan", "morjestarallaa", "terve mieheen", "moikku", "hola", "heissuli", "jassoo", "hejdå", "vieläk sääki elät", "helou", "tervehdys", "terve vaan terve", "tsau", "kuisso", "moikkandeeros", "heip", "moikkanen", "komiaa", "moro nääs", "muija", "tähän käteen", "terveisii", "ehtoota talohon", "hai sie", "huomentapäivää", "tseenare", "aloha", "tere", "jumalan terve", "heipparallaa"]

keyfile = "fiftyheis.keys"
me = "fiftyheis"
api = None
ats = re.compile("@\w+")
url = re.compile("http://\S+")
risu = re.compile("#\S+")


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

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            fulltext = data["text"]
            if fulltext.startswith("RT"):
                print "RT, skipped"
                return
            if data["user"]["screen_name"] == me:
                print "My own tweet"
                return
            text = r.choice(heis) 
            status = text[0].upper() + text[1:] + "!"
            try:
                api.update_status(status=status, in_reply_to_status_id=data["id"])
            except TwythonError:
                api.update_status(status="Sori, ei oikein irtoa (%f)" % time.time())

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

if __name__ == '__main__':
    helper = (TwythonHelper(keyfile))
    api = helper.api
    me = api.get_account_settings()["screen_name"]
    stream = MyStreamer(helper.consumerkey, helper.consumersecret,
                    helper.accesstoken, helper.accesssec)
    stream.statuses.filter(track='@%s' % me)
