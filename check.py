import pvporcupine
from pvrecorder import PvRecorder
import yaml


KEY_FILE = "/Users/brian/.gusgus.yml"
KEYWORDS = list(pvporcupine.KEYWORDS)

def read_yml(path:str)->dict:
    with open(path, "r") as f:
       mappings = yaml.load(f, Loader=yaml.FullLoader)
       return mappings
KEYS = read_yml(KEY_FILE)    


porcupine = pvporcupine.create(access_key=KEYS['picovoice'], keywords=KEYWORDS)
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recoder.start()

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print(f"Detected {KEYWORDS[keyword_index]}")

except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()