from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from random import shuffle
import sys
from wit import Wit

'''
if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
'''
# access_token = sys.argv[1]
access_token = '5W7EUXODL677OTYOLQNUQUXTVVTWHBUC'

print("Hi, I'm Chatty! Please enter a message and I will try to answer.")

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def handle_message(response):
    entities = response['entities']
    name = first_entity_value(entities, 'name')
    age = first_entity_value(entities, 'age_of_person')
    if name:
        return 'Hello ' + name + '!'
    elif age:
        return "Wow, you're {} years old.".format(age)
    else:
        return "I don't know your name"


client = Wit(access_token=access_token)
client.interactive(handle_message=handle_message)