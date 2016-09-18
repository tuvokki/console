#!/usr/bin/env python

import os
import pprint
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from shutil import copyfile

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

disk = '/Volumes/Slim/disk/'
# disk = "/Users/wouter/tmp/test/"
recupdirs = next(os.walk(disk))[1]
# outdir = "/Users/wouter/tmp/out/"
outdir = '/Volumes/Slim/photos/'

pp = pprint.PrettyPrinter(indent=4)

print "-----------------------------------------------------------------------"
for recupdir in recupdirs:
    for file in os.listdir(disk + recupdir):
        if file.endswith(".jpg"):
            src = disk + recupdir + "/" + file
            print("Reading: " + src)
            exif_data = get_exif(src)
            try:
                date_object = datetime.strptime(exif_data['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
                directory = date_object.strftime(outdir + "%Y/%m/%d/")
                newfile = date_object.strftime("%H-%M-%S.jpg")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                dst = directory + newfile
            except Exception, e:
                dst = outdir + "nodate/" + file

            print("Copy to: " + dst)
            copyfile(src, dst)

print "-----------------------------------------------------------------------"
