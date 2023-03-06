import face_recognition
from pathlib import Path

directory = Path('/Users/johanneseder711/Documents/Python/01_active/Keepercam/00_extract_frames/extracted_frames/')

def get_unique_faces(face_encodings, max_distance=0.6):
    unique_face_encodings = []
    for face_encoding in face_encodings:
        # Check if the face encoding is within the maximum distance of any of the unique face encodings
        distances = face_recognition.face_distance(unique_face_encodings, face_encoding)
        if not any(distance <= max_distance for distance in distances):
            unique_face_encodings.append(face_encoding)
    return unique_face_encodings

def count_faces(filenames):
    # Load the images
    images = [face_recognition.load_image_file(filename) for filename in filenames]

    # Find all the faces in the images
    face_locations = [face_recognition.face_locations(image) for image in images]

    # Get the face encodings for the faces
    face_encodings = [face_recognition.face_encodings(image, locations) for image, locations in zip(images, face_locations)]

    # Flatten the array
    face_encodings = [face_encoding for sublist in face_encodings for face_encoding in sublist]
    
    unique_face_encodings = get_unique_faces(face_encodings, max_distance=0.6)

    # Return the number of unique face encodings
    return len(unique_face_encodings)

# Get all the .jpg and .jpeg files in the directory
jpg_files = list(directory.glob('*.jpg'))
jpeg_files = list(directory.glob('*.jpeg'))

# Combine the lists of files
all_files = jpg_files + jpeg_files

# get the list of filenames
filenames = [str(filepath) for filepath in all_files]

# call function to count the number of different faces
count = count_faces(filenames)
print(f'Number of different faces: {count}')

