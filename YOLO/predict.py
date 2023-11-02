from ultralytics import YOLO

model = YOLO('FaceRecognition.pt')  # load a custom model

results = model('image_path')  # predict on an image

names_dict = results[0].names

print(names_dict)

probs = results[0].probs.data

print(probs)

print(names_dict[probs.argmax().item()])