# function to generate ARIMA model and plot train, test, predictions
import matplotlib.pyplot as plt
def model_plot(train=None, test=None, arima_preds=None, title=None):

    plt.figure(figsize=(10,5))
    plt.plot(train, label='Training data')
    if test is not None:
        plt.plot(test, label='Testing data')
    plt.plot(arima_preds, '--', label='Testing preds',color='green')
    plt.legend()
    plt.title(title)
    plt.show()
