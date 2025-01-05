import unittest
import os
import tempfile
from datetime import datetime
import exifread
from organize_photos import organize_photos, get_photo_date

class TestOrganizePhotos(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()
        
        # Create a photo inbox directory
        self.photo_inbox_dir = os.path.join(self.temp_dir, "photo_inbox")
        os.makedirs(self.photo_inbox_dir)
        
        # Create a photos directory
        self.photos_dir = os.path.join(self.temp_dir, "photos")
        os.makedirs(self.photos_dir)
        
        # Create a photos to delete directory
        self.photos_to_delete_dir = os.path.join(self.temp_dir, "photos_to_delete")
        os.makedirs(self.photos_to_delete_dir)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.temp_dir)

    def test_get_photo_date(self):
        # Create a sample photo file with a known EXIF date
        sample_file = os.path.join(self.photo_inbox_dir, "sample.jpg")
        with open(sample_file, "w") as f:
            f.write("Sample content")
        with open(sample_file, "rb") as f:
            tags = exifread.process_file(f, details=False)
        tags['EXIF DateTimeOriginal'] = "2023:10:05 12:34:56"  # Set a specific EXIF date
        with open(sample_file, "wb") as f:
            for tag in tags:
                f.write(f"{tag}: {tags[tag]}\n".encode())
        
        # Get the date of the sample file
        photo_date = get_photo_date(sample_file)
        
        # Verify that the date matches the expected date
        expected_date = datetime(2023, 10, 5, 12, 34, 56)
        self.assertEqual(photo_date, expected_date)

    def test_organize_photos(self):
        # Create a sample photo file with a known creation date (2023-10-05)
        sample_file = os.path.join(self.photo_inbox_dir, "sample.jpg")
        with open(sample_file, "w") as f:
            f.write("Sample content")
        modification_date = datetime(2023, 10, 5)
        os.utime(sample_file, (modification_date.timestamp(), modification_date.timestamp()))
        
        # Call the organize_photos function
        organize_photos(self.photo_inbox_dir, self.photos_dir, self.photos_to_delete_dir)
        
        # Verify that the file has been moved to the correct folder
        target_dir = os.path.join(self.photos_dir, "2023-10")
        self.assertTrue(os.path.exists(target_dir))
        self.assertTrue(os.path.exists(os.path.join(target_dir, "sample.jpg")))
        
        # Verify that the file no longer exists in the photo inbox
        self.assertFalse(os.path.exists(sample_file))

if __name__ == "__main__":
    unittest.main()

