from PIL import Image
import glob

for filepath in glob.iglob(r'/Users/gereltuya/Downloads/coca_cola_copy/*'):
    filename = filepath.replace('/Users/gereltuya/Downloads/', '')

    old_im = Image.open(filename)
    old_size = old_im.size

    new_size = (2000, 2000)
    new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
    new_im.paste(old_im, (int((new_size[0]-old_size[0])/2),
                          int((new_size[1]-old_size[1])/2)))

    # new_im.show()
    new_filename = filename.replace('coca_cola_copy/', 'coca_cola_padded/padded-')
    new_im.save(new_filename)
