import os
import numpy as np
import json


with open('movie17sep.txt', 'r') as f:
     data = f.readlines()

final_data = []
count = 1
for l in data[30:]:
     time, user,movie = l.split(',')
     year = movie[-11:-7]
     movie = movie[:-12].split('/')[-1]
     if user.isnumeric() and year.isnumeric():
        final_data.append({ "id" : count,"user": float(user),"time": time, "movie": movie, "year": float(year)})
        count += 1

json_object = json.dumps(final_data, indent=4)
 
# Writing to sample.json
with open("movie.json", "w") as outfile:
        outfile.write(json_object)

print(outfile[0])


