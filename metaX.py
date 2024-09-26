from PIL import Image
import exifread

#convert GPS coordinates to decimal
def convert_to_degrees(value):
    # Extract degrees, minutes, and seconds from the EXIF GPS tags
    d = float(value.values[0])  # Degrees
    m = float(value.values[1])  # Minutes
    s = float(value.values[2])  # Seconds

    # Calculate the decimal degrees
    return d + (m / 60.0) + (s / 3600.0)

# basic function to extract metadata from an image
def get_basic_metadata(image_path):
    #open image using pillow
    with Image.open(image_path) as img:
        print(f"\n[Basic Image Information]")
        print(f"Image Format: {img.format}")
        print(f"Image Size: {img.size} pixels")
        print(f"Image Mode: {img.mode}\n")

# function to extract EXIF metadata from an image
def get_exif_metadata(image_path):
    #open image in binary mode
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)

        print("[EXIF Metadata]")
        exif_keys = [
            "Image Make", "Image Model", "Image DateTime", 
            "EXIF FNumber", "EXIF ExposureTime", "EXIF ISOSpeedRatings", 
            "EXIF FocalLength", "EXIF LensModel"
        ]
        # loop through the keys and print the corresponding values
        for tag in exif_keys:
            if tag in tags:
                print(f"{tag}: {tags[tag]}")
        
        # extract GPS information if available
        print("\n[GPS Information]")
        gps_latitude = tags.get("GPS GPSLatitude")
        gps_latitude_ref = tags.get("GPS GPSLatitudeRef")
        gps_longitude = tags.get("GPS GPSLongitude")
        gps_longitude_ref = tags.get("GPS GPSLongitudeRef")

        #check if the GPS information is available and convert to decimal
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degrees(gps_latitude)
            lon = convert_to_degrees(gps_longitude)

            #adjust the latitude and longitude based on the reference values
            if gps_latitude_ref.values[0] != 'N':
                lat = -lat
            if gps_longitude_ref.values[0] != 'E':
                lon = -lon
            
            #print the GPS coordinates in decimal format
            print(f"Latitude: {lat:.6f}°")
            print(f"Longitude: {lon:.6f}°")
        else:
            print("No GPS data available.")

if __name__ == "__main__":
    #prompt the user to enter the image path
    image_path = input("Enter the path to the image: ")

    try:
        #extract basic metadata
        print("[+] Extracting basic metadata...")
        get_basic_metadata(image_path)

        print("\n[+] Extracting EXIF metadata...")
        get_exif_metadata(image_path)

    # handle the exception if the image path is invalid
    except FileNotFoundError:
        print("[-] Error: The specified file was not found.")
        
