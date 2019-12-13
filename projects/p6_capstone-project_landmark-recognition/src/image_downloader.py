#!/usr/bin/python

# Note to Kagglers: This script will not run directly in Kaggle kernels. You
# need to download it and run it on your local machine.

# Downloads images from the Google Landmarks dataset using multiple threads.
# Images that already exist will not be downloaded again, so the script can
# resume a partially completed download. All images will be saved in the JPG
# format with 90% compression quality.

import sys, os, multiprocessing, urllib, csv
from PIL import Image
from io import BytesIO
from IPython.display import clear_output


def ParseData(data_file):
  csvfile = open(data_file, 'r')
  csvreader = csv.reader(csvfile)
  key_url_list = [line[:2] for line in csvreader]
  return key_url_list[1:]  # Chop off header


def DownloadImage(key_url_dir):
  #out_dir = sys.argv[2]
  clear_output()
  (key, url, out_dir) = key_url_dir
  filename = os.path.join(out_dir, '%s.jpg' % key)
  print(filename)

  if os.path.exists(filename):
    print('Image %s already exists. Skipping download.' % filename)
    return

  try:
    response = urllib.request.urlopen(url)
    image_data = response.read()
  except:
    print('Warning: Could not download image %s from %s' % (key, url))
    return

  try:
    pil_image = Image.open(BytesIO(image_data))
  except:
    print('Warning: Failed to parse image %s' % key)
    return

  #Convert to RGB and resize :
  try:
    resize_factor = 640/max(pil_image.size) #resize images to 640x480
    new_size = tuple(int(resize_factor*x) for x in pil_image.size)
    pil_image_rgb_resize = pil_image.convert('RGB').resize(new_size)
  except:
    print('Warning: Failed to resize or convert image %s to RGB' % key)
    return

  try:
    pil_image_rgb_resize.save(filename, format='JPEG', quality=90)
  except:
    print('Warning: Failed to save image %s' % filename)
    return


def RunDownloadImage(key_url_dir_list): #Parallel processing and downloading for images
  pool = multiprocessing.Pool(processes=4)
  pool.map(DownloadImage, key_url_dir_list)



#def Run():
#  if len(sys.argv) != 3:
#    print('Syntax: %s <data_file.csv> <output_dir/>' % sys.argv[0])
#    sys.exit(0)
#  (data_file, out_dir) = sys.argv[1:]

#  if not os.path.exists(out_dir):
#    os.mkdir(out_dir)

#  key_url_list = ParseData(data_file)
#  pool = multiprocessing.Pool(processes=50)
#  pool.map(DownloadImage, key_url_list)


#if __name__ == '__main__':
#  Run()
