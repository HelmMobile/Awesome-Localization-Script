#!/usr/bin/python
import re
import json
import os

OPEN_TAG = "<lang>"
CLOSE_TAG = "</lang>"
LOCALE_FILES_PATH = "locales/"
INPUT_FILE_PATH = "index.html"
OUTPUT_FILE_NAME = "index.html"

def translate(textToTranslate, localeFilePath, outputFolder):
    translatedText = textToTranslate
    localeFile = open(localeFilePath, 'r')
    try:
        localeJson = json.load(localeFile)
    except:
        print "Cannot parse file '" + localeFilePath + "'as JSON"
        return

    for key in keys:
        textToSearch = OPEN_TAG + key + CLOSE_TAG
        try:
            textToReplace = localeJson[key]
            translatedText = translatedText.replace(textToSearch, textToReplace.encode('utf-8'))
        except:
            print "ERROR: The key '" + key + "'does not exist"

    translatedFilePath = './' + outputFolder + '/' + OUTPUT_FILE_NAME
    if not os.path.exists(os.path.dirname(translatedFilePath)):
        try:
            os.makedirs(os.path.dirname(translatedFilePath))
        except:
            print "Impossible to create the output file"
            raise

    translatedFile = open(translatedFilePath, 'w')
    translatedFile.write(translatedText)
    translatedFile.close()


baseFile = open(INPUT_FILE_PATH, 'r')
baseHtml = baseFile.read()
baseFile.close()

findKeyRegex = OPEN_TAG + "(.+?)" + CLOSE_TAG
keys = re.findall(findKeyRegex, baseHtml)

for file in os.listdir(LOCALE_FILES_PATH):
    if file.endswith(".json"):
        filename = os.path.splitext(file)[0]
        path = os.path.join(LOCALE_FILES_PATH, file)
        translate(baseHtml, path, filename)
