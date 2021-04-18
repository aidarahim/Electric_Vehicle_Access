import matplotlib.pyplot as plt
def agg_income_plt(df, ytext = None, title = None,
hor_lim = None, ver_lim = None, alpha=0.2):
    fig = plt.figure(figsize=(5,8))
    ax = plt.subplot(111)
    # plot median income with vehicle resale instance
    # plt.figure(figsize=(5,8))
    plt.plot(df.index,df.iloc[:,:100],alpha=alpha)

    # plot median of all incomes, for trend
    plt.plot(df.index,df.mean(axis=1),color='black',linestyle='-',marker='o',ms=10)
    x = range(8)
    plt.xticks(x, ['0','1','2','3','4','5','6','7'])
    plt.xlabel('Resale number')
    plt.ylabel(ytext)
    plt.title(title)
    plt.xlim(hor_lim)
    plt.ylim(ver_lim)
    plt.show()
    fig.savefig('plot.png')
