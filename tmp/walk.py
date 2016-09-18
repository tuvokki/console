#!/usr/bin/env python

import os
import pprint

recupdirs = next(os.walk('/Volumes/Slim/disk/'))[1]
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(recupdirs)
for recupdir in next(os.walk('/Volumes/Slim/disk/'))[1]:
    pp.pprint(recupdir)
