import face_recognition
import cv2

input_video = cv2.VideoCapture("Webcam2.avi")
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

male_image = face_recognition.load_image_file("anas.png")
male_face_encoding = face_recognition.face_encodings(male_image)[0]

known_faces = [
    male_face_encoding
]

face_locations = []
face_encodings = []
face_names = []
frame_number = 0
frameNo = 0
face_names = []
for i in range(3):
    if(i==1):
        frameNo = length/2
    elif(i==2):
        frameNo = length-1

    input_video.set(cv2.CAP_PROP_POS_FRAMES,  frameNo)
    ret, frame = input_video.read()
    frame_number += 1

    if not ret:
        print("err")
        
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        name = False
        if match[0]:
            name = "match"
        
        face_names.append(name)
        
print(face_names)
input_video.release()
cv2.destroyAllWindows()