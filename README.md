# metaX

`metaX` is a Python tool designed to extract metadata (including EXIF data) from image files such as PNG, JPG, and JPEG. The tool can display basic image information (format, size, mode) and extract detailed EXIF metadata including GPS coordinates, camera model, exposure settings, and more.

## Features

- Extract basic metadata (format, size, mode) of the image
- Extract EXIF metadata such as camera make/model, focal length, ISO speed, and more
- Convert GPS coordinates from EXIF metadata into decimal format for easier geolocation

## Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/Dan-Duran/metaX.git](https://github.com/Dan-Duran/metaX.git)
   cd metaX
   ```

2. **Create a Python virtual environment:**

   You can use `venv` to create an isolated Python environment for running `metaX`.

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   ```

3. **Install the required dependencies:**

   ```bash
   pip install Pillow exifread
   ```

## Usage

1. **Run the script:**

   After cloning the repository and installing the dependencies, you can run `metaX` by providing the path to an image file.

   ```bash
   python metaX.py
   ```

   The script will prompt you to enter the path of the image file you'd like to analyze.

2. **Example:**

   ```
   Enter the path to the image: /path/to/image.jpg
   ```

   The tool will output both basic metadata and EXIF metadata, including any GPS data if available.

## Example Output

```
[+] Extracting basic metadata...
[Basic Image Information]
Image Format: JPEG
Image Size: (4032, 3024) pixels
Image Mode: RGB

[+] Extracting EXIF metadata...
[EXIF Metadata]
Image Make: Apple
Image Model: iPhone 12
Image DateTime: 2023:09:15 10:15:30
EXIF FNumber: F/1.8
EXIF ExposureTime: 1/60 sec
EXIF ISOSpeedRatings: 100
EXIF FocalLength: 4.2 mm
EXIF LensModel: iPhone 12 back dual camera 4.2mm f/1.8

[GPS Information]
Latitude: 33.645678°
Longitude: -79.380123°
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

`metaX` is provided as-is, without warranty of any kind. Use it at your own risk. The authors are not responsible for any misuse or damage caused by this tool. Always ensure you have permission to extract metadata from any files you analyze.
