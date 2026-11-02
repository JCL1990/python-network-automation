devices = [
    {"name": "R1", "online": True, "vlan": 10},
    {"name": "R2", "online": False, "vlan": 20},
    {"name": "SW01", "online": True, "vlan": 20},
    {"name": "SW02", "online": False, "vlan": 30},
    {"name": "SW03", "online": False, "vlan": 20}
]

offline_counter = 0

def check_device(device):
    if not device["online"]:
        return "OFFLINE"
    elif device["vlan"] == 30:
        return "VLAN30"
    else:
        return "OK"

for device in devices:
    result = check_device(device)

    if result == "OFFLINE":
        offline_counter = offline_counter + 1

    print(device["name"], result)

print("Devices offline:", offline_counter)
