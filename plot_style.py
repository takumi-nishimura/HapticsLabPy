from matplotlib import pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'  # font familyの設定
plt.rcParams['mathtext.fontset'] = 'stix'  # math fontの設定
plt.rcParams["font.size"] = 15  # 全体のフォントサイズ
plt.rcParams['xtick.labelsize'] = 15  # 軸のフォントサイズ
plt.rcParams['ytick.labelsize'] = 15  # 軸のフォントサイズ
plt.rcParams['xtick.direction'] = 'in'  # x軸のメモリを内側に
plt.rcParams['ytick.direction'] = 'in'  # y軸のメモリを内側に
plt.rcParams['axes.linewidth'] = 1.0  # plotしたときの線幅
plt.rcParams['axes.grid'] = False  # グラフ上にグリッドを表示しない
plt.rcParams["legend.fancybox"] = False  # 凡例を囲う四角が角丸じゃなくなる
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で白いところはスケスケ
plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更
plt.rcParams["legend.handlelength"] = 1  # 凡例の線の長さを調節
plt.rcParams["legend.labelspacing"] = 0.5  # 垂直方向の距離の各凡例の距離
plt.rcParams["legend.handletextpad"] = 1.  # 凡例の線と文字の距離の長さ
plt.rcParams["legend.markerscale"] = 2  # 散布図とかの点のサイズ
plt.rcParams["legend.borderaxespad"] = 0.  # 凡例の端とグラフの端を合わせる

if __name__ == '__main__':
   pass