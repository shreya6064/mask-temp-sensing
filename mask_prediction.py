import tensorflow 
from tensorflow.keras.models import load_model
from keras.preprocessing import image

model = load_model("facemaskdetectionmodel.h5")


def preprocess(sample):
    img_width, img_height = 150,150

    img = image.load_img(sample, target_size = (img_width, img_height))
    img = image.img_to_array(img)
    img = np.array(img).astype('float32')/255
    img = np.expand_dims(img, axis = 0)
    
    pred = model.predict(img)
    return pred[0]

preprocess("test_img_mask.jpg")