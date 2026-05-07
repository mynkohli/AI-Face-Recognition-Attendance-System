import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Correct project path
path = '/Users/mayankkumarkohli/web developer/Face-Recognition-Attendance-System/images'

images = []
classNames = []

# Read image folder
myList = os.listdir(path)

print(myList)

# Load images
for cl in myList:

    imgPath = os.path.join(path, cl)

    curImg = cv2.imread(imgPath)

    if curImg is None:
        print(f"Image not loaded: {cl}")
        continue

    images.append(curImg)

    classNames.append(os.path.splitext(cl)[0])

print(classNames)


# Encode faces
def findEncodings(images):

    encodeList = []

    for img in images:

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:
            encodeList.append(encodings[0])

    return encodeList


# Mark attendance
def markAttendance(name):

    with open('Attendance.csv', 'r+') as f:

        myDataList = f.readlines()

        nameList = []

        for line in myDataList:

            entry = line.split(',')

            nameList.append(entry[0])

        if name not in nameList:

            now = datetime.now()

            dtString = now.strftime('%H:%M:%S')

            dString = now.strftime('%d-%m-%Y')

            f.writelines(f'\n{name},{dtString},{dString}')


# Create encodings
encodeListKnown = findEncodings(images)

print('Encoding Complete')


# Start webcam
cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    if not success:
        print("Camera not working")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)

    encodesCurFrame = face_recognition.face_encodings(
        imgS,
        facesCurFrame
    )

    for encodeFace, faceLoc in zip(
        encodesCurFrame,
        facesCurFrame
    ):

        matches = face_recognition.compare_faces(
            encodeListKnown,
            encodeFace
        )

        faceDis = face_recognition.face_distance(
            encodeListKnown,
            encodeFace
        )

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:

            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc

            y1, x2, y2, x1 = (
                y1 * 4,
                x2 * 4,
                y2 * 4,
                x1 * 4
            )

            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.rectangle(
                img,
                (x1, y2 - 35),
                (x2, y2),
                (0, 255, 0),
                cv2.FILLED
            )

            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2
            )

            markAttendance(name)

    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()