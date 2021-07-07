
from keras.models import load_model
import matplotlib
matplotlib.use("TkAgg")
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Conv2D
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import os
import random
from keras.preprocessing.image import load_img, img_to_array
import pickle 
import sys
print("============= imported stuff =============")

def img_load():
    print("============= loading image =============")
    
    import glob
    import os

    list_of_files = glob.glob('./public/images/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # print(latest_file.name)

    img_path = latest_file
    #img_path = sys.argv[1]
    X_test_noisy = []
    img = load_img(img_path, color_mode='grayscale', target_size=None)
    img = img_to_array(img).astype('float32')/255
    X_test_noisy.append(img)
    X_test_noisy = np.array(X_test_noisy)
    return X_test_noisy
    print("============= image loaded =============")

def model(x_test_noisy):
    print("============= loading model =============")
    model = load_model('deep_conv_model.h5')

    print("============= model loaded =============")
    print("============= predicting output =============")

    output = model.predict(X_test_noisy)
    return output
    print("============= output predicted=============")

def plot(output):
    print("============= printing output =============")
    fig, (ax1,ax2) = plt.subplots(1,2)

    # ax1.imshow(output[0].reshape(600,800), cmap='gray')
    ax1.imshow(X_test_noisy[0], cmap = 'gray')
    ax1.set_title("Your Image")
    ax1.set_xticks([])
    ax1.set_yticks([])

    ax2.imshow(output[0], cmap='gray')
    ax2.set_title("Denoised image")
    ax2.set_xticks([])
    ax2.set_yticks([])
    fig.set_dpi(200)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    import string
    import random
  
    # initializing size of string 
    N = 7
  
    # using random.choices()

    # generating random string for unique filename
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    plt.savefig('./public/images/output/'+res+'.jpg')
    # plt.show()
    # plt.draw()
    # fig.set_dpi(200)

    

    print("usr_in finished.")

X_test_noisy = img_load()
output = model(X_test_noisy)
plot(output)
