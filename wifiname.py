# importing the subprocess module
import subprocess
import os

r = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
ls = r.split("\n")
ssids = [k for k in ls if 'SSID' in k]
print("list of all netwoks with ssid")
print(ssids)

ssids1 = [v.strip() for k, v in (p.split(':') for p in ls if 'SSID' in p)]
print("list of all available networks")
print(ssids1)


# function to connect to a network
def connect(name, SSID):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
    os.system(command)


v1, v2, v3 = [ssids1[i] for i in (0, 1, 2)]
question_prompts = 'The available networks are:\n[1]{}\n[2]{}\n[3]{}\nyour choice is:'.format(v1, v2, v3)
n = input(question_prompts)
for i in n:

    if n == '1':
        name = v1

    elif n == '2':
        name = v2

    elif n == '3':
        name = v3

    else:
        print("invalid choice")
    password = input("enter your password")
    connect(name, name)
