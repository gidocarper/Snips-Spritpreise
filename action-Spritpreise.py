#!/usr/bin/env python3

from hermes_python.hermes import Hermes

USERNAME_INTENTS = "domi"

def user_intent(intentname):
    return USERNAME_INTENTS + ":" + intentname


def subscribe_intent_callback(hermes, intent_message):
    intentname = intent_message.intent.intent_name

    if intentname == user_intent("dieselInfo"):
        pass
    elif intentname == user_intent("benzinInfo"):
        pass

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intents(subscribe_intent_callback).start()
