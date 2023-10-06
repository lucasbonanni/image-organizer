# Photo Organizer

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

The **Photo Organizer** is a Python script that helps you organize your photos by grouping them into folders based on their creation or modification dates. It also checks for duplicate photos and moves them to a separate directory for deletion.

## Features

- Organize photos by year and month of creation/taken date.
- Detect and handle duplicate photos intelligently.
- Customizable source and destination directories.
- Automatic scheduling for periodic organization (e.g., every hour).

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- Required Python libraries (install them using `pip`):
  - `exifread` for reading EXIF data from photos.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Photo-Organizer.git
   ```

### Usage

1. Configure the script by setting the paths for your photo inbox, photos directory, and photos to delete in the `organize_photos.py` script.

2. Run the script to organize your photos:

   ```bash
   python organize_photos.py
   ```

3. The script will move photos from the inbox to folders organized by year and month in the photos directory. Duplicate photos will be moved to the photos to delete directory.

### Scheduling

To run the script periodically (e.g., every hour) on a Linux system, you can use a scheduling tool like `cron`. Here's an example entry for your crontab:

```bash
0 * * * * /usr/bin/python3 /path/to/organize_photos.py
```

Make sure to replace `/usr/bin/python3` with the path to your Python interpreter and `/path/to/organize_photos.py` with the full path to your script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [exifread](https://pypi.org/project/ExifRead/) library for helping extract photo creation dates.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request.

## Author

- [Lucas Bonanni](https://github.com/lucasbonanni)

## Contact

If you have any questions or suggestions, feel free to contact me at your.email@example.com.

```

Remember to replace placeholders such as `yourusername`, `Your Name`, and `your.email@example.com` with your actual information. You can also add more sections or customize the README to suit your project's specific needs.
