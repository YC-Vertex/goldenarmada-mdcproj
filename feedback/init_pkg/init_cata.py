# pylint: disable=no-member
import numpy as np
import tensorflow as tf
import keras
import cv2

### quotes:
# https://blog.csdn.net/geyalu/article/details/50190121

def inverse(image): 
    '''
    :param image: 以数组形式存储的图片数据（单通道2维，即长乘宽）
    :return: 反色后的数组形式存储的图片数据

    I use this function to inverse the color of a image, because:
    a. cv2.normalize will make the background all white and content all black, but
    b. the CNN requires the picture to have black background and white content.
    '''
    height,width = image.shape
    inversed = image.copy()
    for i in range(height):
        for j in range(width):
            inversed[i,j] = (255-image[i,j]) 
    return inversed

def read_my_data(my_img_path):
    '''
    :param my_img_path: a string, the location of the img
    :return: numpy array of size (1,28,28,1), to be fed into CNN
    '''
    img = cv2.imread(my_img_path,0) # 灰度方式读取图片原始信息，2维，原始长乘宽
    img = cv2.Canny(img,20,65) # 将图片处理成边缘形式，shape不变（这步≈正则化+反色，但是效果不太一样）
    img = cv2.normalize(img,dst=None,alpha=300,beta=10,norm_type=cv2.NORM_MINMAX) # 正则化提升对比度，shape不变
    img = cv2.resize(img, (28,28)) # 大小resize为28*28
    # img = inverse(img) # 反色操作，shape不变
    # cv2.imshow('图',img) # 展示图片
    # cv2.waitKey(0) # 展示图片，暂停
    my_test_x = img.astype('float32')/255 # 模型要求的归一化
    my_test_x = my_test_x[np.newaxis,:,:,np.newaxis] # 模型要求的维度扩张，最终维度为(1,28,28,1)
    return my_test_x

def newargmax(prediction):
    '''
    :param prediction: 对衣服类别的预测结果，对每个category（共10个，包括鞋包等无用category）提供一个数值置信度
    :return: 类别标签，0短袖、1裤子、2长袖
    '''
    valid_index = [0,1,2,4,6]
    maxpi = -100000
    res = -1
    for i in valid_index:
        if prediction[i] >= maxpi:
            maxpi = prediction[i]
            res = i
    if res==4 or res==6:
        res = 2
    return res

def cata(img_path):
    """
    :lib: feedback
    :func: cata
    :param: img_path
    :return: res (category tag)

    Return the category tag of a image, given the image path. 
    """
    try:
        # 加载本地图片
        my_test_x = read_my_data(img_path)
    except:
        print("data error: failed to read data.")
    else:
        try:
            # 加载本地模型
            loaded_model = keras.models.load_model("path/model.h5")
        except:
            print("model error: failed to load CNN model.")
        else:
            # 使用模型进行预测
            try:
                y_pred = loaded_model.predict(my_test_x, batch_size=1) # 预测我的数据
            except:
                print("model error: failed to make prediction.")
            else:
                # 输出预测结果
                res = newargmax(y_pred[0])
    return res
