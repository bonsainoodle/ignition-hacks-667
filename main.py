from xmlrpc.server import SimpleXMLRPCDispatcher
import soundcard as sc
import soundfile as sf

# OUTPUT_FILE_NAME = "out.wav"  # file name.
# SAMPLE_RATE = 48000  # [Hz]. sampling rate.
# RECORD_SEC = 5  # [sec]. duration recording audio.
# CHUNK = 1024  # [byte]. chunk size.

# data = []

# with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
#     samplerate=SAMPLE_RATE
# ) as mic:

#     # # record audio with loopback from default speaker.
#     while True:
#         stream = mic.record(numframes=CHUNK).tolist()

#         for frame in stream:
#             data.append(frame)

#     # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
#     sf.write(file=OUTPUT_FILE_NAME, data=data, samplerate=SAMPLE_RATE)

speakers = sc.all_speakers()

source = None

for index, speaker in enumerate(speakers):
    print(f"{index} : {speaker.name}")

choice = int(input("Select a source: "))

try:
    if choice > 0:
        source = speakers[choice]
    else:
        raise IndexError
except IndexError:
    print("Invalid choice")
    exit()

print(source)
