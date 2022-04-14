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
        self.buffer = np.frombuffer(in_data, dtype='int16')/32768.0
        self.audio_array = np.append(self.audio_array,self.buffer)
        self.fft()
        self.amp = np.abs(self.F/(self.CHUNK/2))
        self.vol = sum(self.amp[25:128])
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
        self.d2ym = np.array([])
        self.d3y = 0
        self.d3ym = 0

        self.maxfft = np.zeros(self.rate)

    def visualize(self):
        if self.d3y > self.d3ym:
            self.m_t = time.perf_counter()
            self.d2ym = self.d2y
            self.d3ym = self.d3y
        if time.perf_counter() - self.m_t > 2:
            self.d3ym = 0

        self.grid_x = 3
        self.grid_y = 2

        plt.clf()

        plt.subplot2grid((self.grid_x,self.grid_y),(0,0),colspan=self.grid_x)
        plt.plot(self.d1x,self.d1y)
        plt.axis([0, 1, -0.8, 0.8])
        plt.xlabel("time [sample]")
        plt.ylabel("amplitude")
        
        plt.subplot2grid((self.grid_x,self.grid_y),(2,0))
        plt.plot(self.d2x[1:int(self.chunk/2)], self.d2y[1:int(self.chunk/2)])
        plt.plot(self.d2x[1:int(self.chunk/2)], self.d2ym[1:int(self.chunk/2)], color='black', linestyle='dashed', linewidth = 1.0)
        plt.axis([0, 500, 0, 0.1])
        plt.xlabel("freq [Hz]")
        plt.ylabel("amplitude")

        plt.subplot2grid((self.grid_x,self.grid_y),(2,1))
        plt.bar(1,self.d3y)
        plt.hlines(self.d3ym, 0, 2, "blue", linestyles='dashed')
        plt.axis([0, 2, 0, 1])
        plt.xlabel("intensity")

        plt.pause(0.001)

    def plot_close(self):
        plt.clf()
        plt.close()

class KEYINPUT:
    def __init__(self) -> None:
        self.k_flag = 0

    def input_waiting(self):
        sleepflag = 0
        while True:
            kb = input()
            if kb == 'r':
                print('!!!recording start!!!')
                if sleepflag == 0:
                    time.sleep(0.8)
                    sleepflag = 1
                else:
                    pass
                self.k_flag = 1
            if kb == 'p':
                print('!!!playback start!!!')
                self.k_flag = 2
            if kb == 'q':
                print('!!!stop!!!')
                break

if __name__ == "__main__":
    search = SEARCH()

    ai = AUDIOINPUT()

    pl = PLOT(ai.rate,ai.CHUNK)

    ki = KEYINPUT()
    kt = threading.Thread(target=ki.input_waiting)
    kt.start()
    print('r:recording,  p:playback')

    while True:
        try:
            if ki.k_flag == 1:
                ki.k_flag = 0
                ai.stream.start_stream()

                while kt.is_alive():
                    try:
                        pl.d1y = ai.audio_array[-ai.rate:]
                        pl.d2y = ai.amp
                        pl.d3y = ai.vol
                        pl.visualize()
                    except:
                        ai.stream.stop_stream()

                ai.close()
                print()
                print("finish")
                pl.plot_close()
                break
            elif ki.k_flag == 2:
                print('p')
                ki.k_flag = 0
                while kt.is_alive():
                    try:
                        print('play')
                    except KeyboardInterrupt:
                        break
            else:
                pass
        except KeyboardInterrupt:
            break