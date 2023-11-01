import os
import api_ends

for x in os.listdir('./recommendations/'):
    name = x.split('_')[0]
    api_ends.get_comics(name)