from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('/home/pi/Resume_Project/Photos/image.jpg'))
hash1 = imagehash.average_hash(Image.open('/home/pi/Resume_Project/Photos/image4.jpg'))
#hash1 = imagehash.average_hash(Image.open('/home/pi/Resume_Project/Photos/image2.jpg'))
#hash1 = imagehash.average_hash(Image.open('/home/pi/Resume_Project/Photos/image3.jpg'))
#hash1 = imagehash.average_hash(Image.open('/home/pi/Resume_Project/Photos/cat.jpg'))
cutoff = 20 #maximum bits that could be different between the hashes.

if hash0 - hash1 < cutoff:
    print('images are similar')
else:
    print('images are not similar')
