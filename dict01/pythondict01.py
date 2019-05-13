#! /usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1","version":"1.2","vendor":"cisco"}
(switch["hostname"])
#print(switch["lynx"])
#print(switch.get('lynx',"The key is in another castle")
#)
print(switch.get('version'))
print(switch.keys())
print(switch.values())
switch['adminlogin'], switch['password'] = 'ven08','qwerty' 
print(switch)

        

