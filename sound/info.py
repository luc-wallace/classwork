from scipy.io import wavfile

samplingRate, soundData = wavfile.read("StarWars3.wav")

print(samplingRate)

for i in soundData:
    print(i)

print(samplingRate)
