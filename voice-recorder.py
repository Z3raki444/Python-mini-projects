import sounddevice as sd  # Library for recording and playing sound
from scipy.io.wavfile import write  # Function to save audio as a WAV file
import wavio as wv  # Alternative library for saving WAV files

# Set the sampling frequency (number of samples per second)
freq = 44100  # Standard for high-quality audio

# Set the duration of the recording in seconds
duration = 5  # Recording will last for 5 seconds

# Start recording audio with the specified duration, frequency, and stereo channels (2 channels)
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Wait for the recording to finish
sd.wait()

# Save the recording as a WAV file using scipy's write function
write("recording.wav", freq, recording)

# Save the recording as a WAV file using the wavio library (alternative method)
# The parameter 'sampwidth' specifies the sample width in bytes (2 bytes for 16-bit audio)
wv.write("recording.wav", recording, freq, sampwidth=2)