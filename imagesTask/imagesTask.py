import os
from PIL import Image, ExifTags

img_folder = r"C:\Users\zidan\Desktop\GISProj\Images"

img_contents = os.listdir(img_folder)

for img in img_contents:
    print(img)
    full_path = os.path.join(img_folder, img)
    # printing full path
    print(full_path)
    pillow_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
    # printing exif tags
    print exif
    gpsInfo = {}
    try:
        for key in exif['GPSInfo'].keys():
            decoded_value = ExifTags.GPSTAGS.get(key)
            gpsInfo[decoded_value] = exif['GPSInfo'][key]

        long_ref = gpsInfo.get('GPSLongitudeRef')
        long = gpsInfo.get('GPSLongitude')
        lt_ref = gpsInfo.get('GPSLatitudeRef')
        lat = gpsInfo.get('GPSLatitude')

        print long_ref, " : ", long
        print lt_ref, " : ", lat

    except:
        print "this image has no GPS info in it{}".format(full_path)


