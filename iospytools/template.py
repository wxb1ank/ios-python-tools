import re
import json
import os

from .ipsw import IPSW
from .iphonewiki import iPhoneWiki
from .ipswapi import APIParser
from .manifest import Manifest

"""

This will handle the key template stuff from iphonewiki (webpage)

"""

"""

This is the key template for the key pages. When a page uses this template, it is added to the Key Pages category.

Syntax:

If the device is not an iPhone or a cellular iPad, delete the Baseband parameter.

If the device is an Apple TV (iOS versions), set Version to the marketing version with the internal version in parenthesis.

For each *, *IV, and *Key section, put the file name on the first line. If the item is the Root FS or a ramdisk, remove the .dmg
file extension. If that firmware item does not exist in that firmware, delete its parameter section. If the firmware item is not encrypted,
set *IV to "Not Encrypted" and delete the *Key parameter. If the key/iv is not known, then the KBAG should be added.

For devices such as iPhone 6s that have two sets of files such as N71AP and N71mAP, then a second file can be added underneath
with a "2" at the end of the name. For example, you can have AppleLogo and AppleLogo2 blocks.

For DownloadURL, do not place anything other than URLs to free firmwares hosted on Apple Inc.'s servers. For beta firmwares, delete the parameter.

"""

class Template(object):
    def __init__(self, device=None, version=None, manifest='BuildManifest.plist'):
        super().__init__()

        self.device = device
        self.version = version
        self.manifest = manifest

    def parseTemplate(self):
        with open('key-template-img3.txt') as f:
            data = f.read()
            keys = data.split('{{keys')[1].split('}}')[0].replace('|', '').splitlines()
            new_list = list(filter(None, keys)) # Remove all ''

            head = list()
            body = list()

            for stuff in new_list:
                fix = re.sub('\s+',' ', stuff)[:-2].strip()
                if fix == 'RootFS': # YASSSSS Got it working :D
                    break
                else:
                    head.append(fix)

        template = {
            'template': {
                'head': head,
                'keys': {
                    'filename',
                    'iv',
                    'key',
                    'kbag'
                }
            }
        }

        print(template)

        f.close()

    def initTemplateFromIPSW(self):
        pass
