import urllib3
import hashlib
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import time
import os


path_to_dir = input("Enter the path to your trainB folder:\n")
num_to_download = int(input("Enter how many images you'd like to download:\n"))

# We'll keep a set of our image hashcodes to prevent downloading duplicates.
hashes = set()

html = urllib3.PoolManager(1)

# Going to the /image endpoint just gives us solely image data, no other html.
url = "https://thispersondoesnotexist.com/image"

i = 0
while i < num_to_download:
    
    res = html.request("GET", url, preload_content=False)
    
    # Run a hash function on the bytes data to check for duplicate images.
    hashcode = hashlib.sha1(res.data).hexdigest()
    
    if hashcode in hashes:
        continue
    else:
        hashes.add(hashcode)

    # We need to treat the data like a file for PIL to be able to read it.
    # We're not reading using OpenCV because it couldn't read the IO object :(
    img = np.array(Image.open(BytesIO(res.data)))
    
    # All of our faces from Labeled Faces in the Wild were 250px, so let's
    # resize these ones to match.
    resized = cv2.resize(img, (250, 250))
    
    
    fname = os.path.join(path_to_dir, f"{i:05d}.jpg")
    
    # OpenCV uses BGR instead of RGB, so we need to convert between the two.
    cv2.imwrite(fname, cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))
        
        
    i += 1
    
    time.sleep(1)