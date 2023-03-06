import face_recognition
from pathlib import Path

# declare the Path to the reference image
refence_image_path = Path('/Users/johanneseder711/Documents/Python/01_active/Keepercam/00_extract_frames/extracted_frames/frame_at_0min41sec.jpg')

# load the image 
refence_image = face_recognition.load_image_file(str(refence_image_path))

# Find all the faces in the images
face_locations = [face_recognition.face_locations(image) for image in refence_image]

# Get the face encodings for the faces
face_encodings = [face_recognition.face_encodings(image, locations) for image, locations in zip(refence_image, face_locations)]