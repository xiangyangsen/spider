import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seabron as sns
import re
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# import jieba
# import os
# from PIL import Image
# from os import path
from decimal import *
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D




#清洗数据，转换PV过万的数据
def view_to_num(item):
    m = re.search('.*?(万)',item['view'])#找到PV过万的数据
    if m:    #进行数据修正
        ns = item['view'][:-1]
        nss = Decimal(ns)*10000
    else:    #不处理
        nss = item['view']
    return int(nss)

def parse_woshipm():

    csv_file = '/Users/flu/Downloads/woshipm.csv'
    csv_data = pd.read_csv(csv_file, low_memory=False)
    csv_df = pd.DataFrame(csv_data)
    print(csv_df)

    print(csv_df.shape)
    print(csv_df.info())
    print(csv_df.head())

    csv_df['date'] = pd.to_datetime(csv_df['date'])

    csv_df['view_num'] = csv_df.apply(view_to_num,axis = 1)
    print(csv_df.info())



    data_duplicated = csv_df.duplicated().value_counts()
    print(data_duplicated)

    data = csv_df.drop_duplicates(keep='first')

    data = data.reset_index(drop=True)

    data['title_length'] = data['title'].apply(len)

    data['garp_length'] = data['garp'].apply(len)

    data['year'] = data['date'].dt.year

    print(data.describe())

    print(data['author'].describe())
    print(data['date'].describe())


    # x = data['title_length']
    # y = data['view_num']
    #
    # plt.title('title length VS view number')
    # plt.xlabel("x axis caption")
    # plt.ylabel("y axis caption")
    # plt.plot(x, y, "ob")
    # plt.show()

    x = data['garp_length']
    y = data['bookmark']

    plt.scatter(x,y,alpha=0.25,marker='.')
    plt.title('garp_length VS bookmark')
    plt.xlabel("garp_length")
    plt.ylabel("bookmark")
    # plt.grid(True)
    plt.show()

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    #
    # # Make data.
    # X = garp_length
    # Y = title_length
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = bookmark
    #
    # # Plot the surface.
    # surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
    #                        linewidth=0, antialiased=False)
    #
    # # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    #
    # # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    #
    # plt.show()






if __name__ == '__main__':
    parse_woshipm()


