import cv2


emotions = ['neutral', 'anger', 'disgust', 'happy', 'sadness', 'surprise']
CLASSIFIER_DATA_FILE = "./models/fishface_trained_classifier.xml"


def predict_emotion(cropped_face):
    fishface = cv2.createFisherFaceRecognizer()
    try:
        fishface.load(CLASSIFIER_DATA_FILE)
    except:
        print ("classifier data file not found")

    prediction, confidence = fishface.predict(cropped_face)
    print ("predicted emotion: " + emotions[prediction], " (confidence: " + str(confidence) + ")")
    return emotions[prediction]