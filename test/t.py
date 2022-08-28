import sounddevice as sd

devs = sd.query_devices()

print(devs)
