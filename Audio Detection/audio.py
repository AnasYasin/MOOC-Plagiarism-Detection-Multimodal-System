import pyaudio
import wave
from array import array
import sys

wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()

FORMAT=p.get_format_from_width(wf.getsampwidth())
CHANNELS=wf.getnchannels()
RATE=wf.getframerate()
CHUNK=1024
THRESHOLD=7500

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

counter = 0
talking = 0
while(True):
    counter+=1
    data = wf.readframes(CHUNK)
    data_chunk=array('h',data)
    try:
        vol=max(data_chunk)
    except:
        break
    if(vol>=THRESHOLD):
        print("something said______________________________________________________________________________________________")
        talking+=1
    else:
        print("nothing")
    print("\n")
    stream.write(data)

print("_______________________________")
print(talking/counter)
if((talking/counter) >= 0.15):
    print("Plag")
else:
    print("No Plag") 

stream.stop_stream()
stream.close()
p.terminate()   