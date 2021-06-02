import face_recognition
from PIL import Image, ImageDraw


image1 = face_recognition.load_image_file('fngel.jpg')
image1_encode = face_recognition.face_encodings(image1)[0]


image2 = face_recognition.load_image_file('shaian.jpg')
image2_encode = face_recognition.face_encodings(image2)[0]


known_face_encoding = [
    image1_encode,
    image2_encode
]


known_face_names = [
    "Angel",
    "shaian"
]


test_image = face_recognition.load_image_file('unk1.jpg')
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)


pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

      
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
    print (matches)


    name = "Unknown Person"


    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    draw.rectangle(((left,top), (right, bottom)), outline = (0,0,0))


    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0,0,0), outline = (0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill = (255,255,255,255))


del draw


pil_image.show()