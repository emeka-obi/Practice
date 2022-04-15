def name_devices(device_list):
    unique_devices = []
    device_dict = {}
    for device in device_list:
        if device not in device_dict:
            device_dict[device] = 1
            unique_devices.append(device)
        else:
            updated_name = device + str(device_dict[device])
            unique_devices.append(updated_name)
            device_dict[device] = device_dict[device] + 1
    return unique_devices
