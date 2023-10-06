import os
import shutil
import filecmp
from datetime import datetime
import exifread  # You'll need to install this library using pip


def get_photo_date(file_path):
    # Open the image file for reading EXIF data
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    
    # Check for EXIF tags that contain the date the photo was taken/created
    for tag in ('EXIF DateTimeOriginal', 'Image DateTime', 'EXIF DateTimeDigitized'):
        if tag in tags:
            date_str = str(tags[tag])
            return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    
    # If no EXIF date is found, use the file modification date
    return datetime.fromtimestamp(os.path.getmtime(file_path))


def organize_photos(photo_inbox_dir, photos_dir, photos_to_delete_dir):
    files = os.listdir(photo_inbox_dir)
    
    for file in files:
        source_path = os.path.join(photo_inbox_dir, file)
        if os.path.isfile(source_path):
            # Get the date the photo was taken/created
            photo_date = get_photo_date(source_path)
            
            # Create the target directory path using the year and month
            target_dir = os.path.join(photos_dir, photo_date.strftime("%Y-%m"))
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            target_path = os.path.join(target_dir, file)

            # Check if a file with the same name exists in the target directory
            if os.path.exists(target_path):
                # Compare the source and target files using filecmp
                if filecmp.cmp(source_path, target_path):
                    # If they are the same, move the source file to the photos_to_delete directory
                    delete_target_path = os.path.join(photos_to_delete_dir, file)
                    shutil.move(source_path, delete_target_path)
                    print(f"Moved duplicate file {file} to {photos_to_delete_dir}")
                else:
                    # If they are different, rename the source file to avoid overwriting
                    file_name, file_extension = os.path.splitext(file)
                    new_file_name = f"{file_name}_{photo_date.strftime('%Y%m%d%H%M%S')}{file_extension}"
                    new_target_path = os.path.join(target_dir, new_file_name)
                    shutil.move(source_path, new_target_path)
                    print(f"Renamed and moved {file} to {target_dir}/{new_file_name}")
            else:
                # If no file with the same name exists, simply move it to the target directory
                shutil.move(source_path, target_path)
                print(f"Moved {file} to {target_dir}")

if __name__ == "__main__":
    photo_inbox_dir = "/media/photo_inbox"
    photos_dir = "/media/photos"
    photos_to_delete_dir = "/media/photos_to_delete"
    
    organize_photos(photo_inbox_dir, photos_dir, photos_to_delete_dir)

