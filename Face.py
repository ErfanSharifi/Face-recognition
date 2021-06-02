import PIL.ImageDraw
import face_recognition
import PIL.Image

image = face_recognition.load_image_file("old.jpg")

# face_encoding = face_recognition.face_encodings(image)
# print (face_encoding)

face_locations = face_recognition.face_locations(image)
print (face_locations)
# num_face = len(face_locations)


# print ("I Found {} faces in image". format(num_face))


# pil_image = PIL.Image.fromarray(image)
# print (pil_image)


# for face_location in face_locations:

#     top, right, bottom, left = face_location
#     draw = PIL.ImageDraw.Draw(pil_image)
#     draw.rectangle([left, top, right, bottom], outline = "red")

# pil_image.show()