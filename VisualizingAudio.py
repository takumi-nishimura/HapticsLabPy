import pyaudio
import numpy as np
import time
import threading
import matplotlib.pyplot as plt

class SEARCH:
    def __init__(self) -> None:
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            print(info)

    def get_input_device(self):
        input_index_list = []
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            if not info['maxInputChannels'] == 0:
                input_index_list.append(info['index'])
        print(input_index_list)
        return input_index_list

    def get_output_device(self):
        output_index_list = []
        for i in range(self.p.get_device_count()):
            info = self.p.get_device_info_by_index(i)
            if not info['maxOutputChannels'] == 0:
                output_index_list.append(info['index'])
        print(output_index_list)
        return output_index_list

class AUDIOINPUT:
    def __init__(self) -> None:
        self.audio_array = np.array([])

        self.p = pyaudio.PyAudio()
        self.channels = 1
        self.rate = 16000
        self.CHUNK = 2**12
        self.format = pyaudio.paInt16
        self.stream = self.p.open(
                        format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        frames_per_buffer=self.CHUNK,
                        input=True,
                        stream_callback=self.callback)

    def callback(self, in_data, frame_count, time_info, statuss):
        self.buffer = np.frombuffer(in_data, dtype='int16')
        self.audio_array = np.append(self.audio_array,self.buffer)
        self.fft()
        return (in_data, pyaudio.paContinue)

    def close(self):
        self.stream.close()
        self.p.terminate()

    def fft(self):
        self.freq = np.fft.fftfreq(self.CHUNK, d=1.0/self.rate)
        self.F = np.fft.fft(self.buffer)

class PLOT:
    def __init__(self,rate,chunk) -> None:
        self.rate = rate
        self.chunk = chunk
        self.d1x = np.arange(0, self.rate)/self.rate
        self.d1y = np.array([])
        self.d2x = np.fft.fftfreq(self.chunk,d=1.0/self.rate)
        self.d2y = np.array([])
        self.maxfft = np.zeros(self.rate)

    def visualize(self):
        self.grid_x = 2
        self.grid_y = 2

        plt.clf()

        plt.subplot2grid((self.grid_x,self.grid_y),(0,0),colspan=self.grid_x)
        plt.plot(self.d1x,self.d1y/32768.0)
        plt.axis([0, 1, -1, 1])
        plt.xlabel("time [sample]")
        plt.ylabel("amplitude")

        plt.pause(0.001)

class KEYINPUT:
    def __init__(self) -> None:
        self.k_flag = 0

    def input_waiting(self):
        sleepflag = 0
        while True:
            kb = input()
            if kb == 's':
                print('!!!start!!!')
                if sleepflag == 0:
                    time.sleep(0.5)
                    sleepflag = 1
                else:
                    pass
                self.k_flag = 1
            if kb == 'q':
                print('!!!stop!!!')
                break
            if kb == 'r':
                print('---reflesh---')
                self.k_flag = 2

if __name__ == "__main__":
    search = SEARCH()

    ai = AUDIOINPUT()

    pl = PLOT(ai.rate,ai.CHUNK)

    ki = KEYINPUT()
    kt = threading.Thread(target=ki.input_waiting)
    kt.start()
    print('s:start')

    while True:
        try:
            if ki.k_flag == 1:
                ki.k_flag = 0
                ai.stream.start_stream()

                while kt.is_alive():
                    try:
                        pl.d1y = ai.audio_array[-ai.rate:]
                        pl.visualize()
                        if ki.k_flag == 2:
                            print('reflesh')
                            ki.k_flag = 0
                    except KeyboardInterrupt:
                        ai.stream.stop_stream()
                ai.close()
                print()
                print("finish")
                break
            else:
                pass
        except KeyboardInterrupt:
            break