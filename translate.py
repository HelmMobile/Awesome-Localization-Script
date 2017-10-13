#!/usr/bin/python
import re
import json
import os

OPEN_TAG = "<lang>"
CLOSE_TAG = "</lang>"
LOCALE_FILES_PATH = "../assets/locales/"
INPUT_FILE_PATH = "index.html"
OUTPUT_FILE_NAME = "index.html"

def translateTo(language):
    translatedHtml = baseHtml
    translationFilePath = TRANSLATION_FILES_PATH + language + '.json'
    translationFile = open(translationFilePath, 'r')
    translationJson = json.load(translationFile)

    for key in keys:
        textToSearch = OPEN_TAG + key + CLOSE_TAG
        try:
            textToReplace = translationJson["token"][key]
            translatedHtml = translatedHtml.replace(textToSearch, textToReplace.encode('utf-8'))
        except:
            print "ERROR: The key '" + key + "'does not exist"

    translatedFilePath = './' + language + '/' + OUTPUT_FILE_NAME
    if not os.path.exists(os.path.dirname(translatedFilePath)):
        try:
            os.makedirs(os.path.dirname(translatedFilePath))
        except:
            print "Impossible to create the output file"
            raise

    translatedFile = open(translatedFilePath, 'w')
    translatedFile.write(translatedHtml)
    translatedFile.close()


baseFile = open(BASE_FILE_PATH, 'r')
baseHtml = baseFile.read()
baseFile.close()

findKeyRegex = OPEN_TAG + "(.+?)" + CLOSE_TAG
keys = re.findall(findKeyRegex, baseHtml)

translateTo('es')
translateTo('ca')
translateTo('en')
