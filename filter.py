from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

#バターワースフィルタ（ローパス）
def lowpass(x, samplerate, fp, fs, gpass, gstop):
    fn = samplerate / 2                           #ナイキスト周波数
    wp = fp / fn                                  #ナイキスト周波数で通過域端周波数を正規化
    ws = fs / fn                                  #ナイキスト周波数で阻止域端周波数を正規化
    N, Wn = signal.buttord(wp, ws, gpass, gstop)  #オーダーとバターワースの正規化周波数を計算
    b, a = signal.butter(N, Wn, "low")            #フィルタ伝達関数の分子と分母を計算
    y = signal.filtfilt(b, a, x)                  #信号に対してフィルタをかける
    return y                                      #フィルタ後の信号を返す

samplerate = 25600
x = np.arange(0, 2560) / samplerate  # 波形生成のための間軸の作成
data = np.sin(2.0 * np.pi * 50 * x) + 0.3 * np.random.normal(loc=0, scale=1, size=len(x)) #サイン波にガウシアンノイズを重畳
 
fp = 200       #通過域端周波数[Hz]
fs = 400       #阻止域端周波数[Hz]
gpass = 3      #通過域端最大損失[dB]
gstop = 40     #阻止域端最小損失[dB]

data_filt = lowpass(data, samplerate, fp, fs, gpass, gstop)

plt.plot(x, data)
plt.plot(x, data_filt)
plt.show()