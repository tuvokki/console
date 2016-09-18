#!/usr/bin/env python

import os
outdir = '/Volumes/Slim/photos/'
outdir2 = '/Volumes/Slim/photos2/'

cpt = sum([len(files) for r, d, files in os.walk(outdir)])
cpt2 = sum([len(files) for r, d, files in os.walk(outdir2)])

print(cpt)
print(cpt2)
