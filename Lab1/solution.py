import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


correlation1 = pd.read_csv('stock/AIR-TDG_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation2 = pd.read_csv('stock/BCH_USD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation3 = pd.read_csv('stock/BMW-TDG_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation4 = pd.read_csv('stock/BTC_USD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation5 = pd.read_csv('stock/ETH_USD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation6 = pd.read_csv('stock/LTC_USD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation7 = pd.read_csv('stock/NFLX-RM_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                '<CLOSE>', '<VOL>'])
correlation8 = pd.read_csv('stock/NKE-RM_TQBD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                    '<CLOSE>', '<VOL>'])
correlation9 = pd.read_csv('stock/NVDA-RM_TQBD_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                     '<CLOSE>', '<VOL>'])
correlation10 = pd.read_csv('stock/VOW3-TDG_220101_221124.csv', sep=',', usecols=['<OPEN>', '<HIGH>', '<LOW>',
                                                                                  '<CLOSE>', '<VOL>'])


def show_heat_map(title, data):
    plt.figure(figsize=(5, 5))
    sns.heatmap(data.corr(), center=0, cmap='Blues', annot=True)
    plt.title(title, fontsize=17)
    plt.show()


show_heat_map('AIR-TDG', correlation1)
show_heat_map('BCH_USD', correlation2)
show_heat_map('BMW-TDG', correlation3)
show_heat_map('BTC_USD', correlation4)
show_heat_map('ETH_USD', correlation5)
show_heat_map('LTC_USD', correlation6)
show_heat_map('NFLX-RM', correlation7)
show_heat_map('NKE-RM_TQBD', correlation8)
show_heat_map('NVDA-RM_TQBD', correlation9)
show_heat_map('VOW3-TDG', correlation10)


