import numpy
import sys
from PIL import Image
import glob

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

for filepath in glob.iglob(r'/Users/gereltuya/Downloads/coca_cola_copy/*'):
    filename = filepath.replace('/Users/gereltuya/Downloads/', '')

    img = Image.open(filename)
    width, height = img.size
    m = -0.5
    xshift = abs(m) * width
    new_width = width + int(round(xshift))
    img = img.transform((new_width, height), Image.AFFINE,
            (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)

    new_filename = filename.replace('coca_cola_copy/', 'coca_cola_pers/pers-')
    img.save(new_filename)
    print('image saved at', new_filename)
