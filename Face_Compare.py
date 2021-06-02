import face_recognition
import PIL.ImageDraw
from face_recognition.api import face_encodings
import PIL.Image

image1 = face_recognition.load_image_file("fateme.jpg")
image1_encode = face_recognition.face_encodings(image1)[0]
known_face = [image1_encode]

unkown_image = face_recognition.load_image_file("unk1.jpg")
unkown_image_decode = face_recognition.face_encodings(unkown_image)



for i in unkown_image_decode:

    resualt = face_recognition.compare_faces(known_face, i, tolerance= 0.6)


    name = "Unknown"

    if resualt[0]:
        name = "Fateme"
        face_locations = face_recognition.face_locations(unkown_image)

        
    print (f"i find {name}")