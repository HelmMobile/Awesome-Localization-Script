# Awesome localization script [![Python version](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)

A simple python script to translate any file to different languages providing locale files in JSON format.

### Prerequisites

You need to install python to run the script

You can download it [here](https://www.python.org/downloads/)

### Usage

Add tags and keys to the file that you want to translate:

```html
<lang>key</lang>
```

#### Example
`index.html`

```html
<li>
  <a href="#services" class="scrollto"><lang>services</lang></a>
</li>
<li>
  <a href="#motivation" class="scrollto"><lang>motivation</lang></a>
</li>
<li>
  <a href="#projects" class="scrollto"><lang>projects</lang></a>
</li>
<li>
  <a href="#team" class="scrollto"><lang>team</lang></a>
</li>
<li>
  <a href="#contact" class="scrollto"><lang>contact</lang></a>
</li>
```

Create `locales` folder

Add the locale files to the folder, use the format shown below to add the key and translations, and save the file as `.json`:

```json
{
  "key": "translation"
}
```

#### Example

`ca.json`

```json
{
  "services": "Serveis",
  "motivation": "Motivació",
  "projects": "Projectes",
  "team": "Equip",
  "contact": "Contacte",
}
```

Check the configuration of the script, you can change the following options:
```python
OPEN_TAG = "<lang>"
CLOSE_TAG = "</lang>"
LOCALE_FILES_PATH = "locales/"
INPUT_FILE_PATH = "index.html"
OUTPUT_FILE_NAME = "index.html"
```

* **OPEN_TAG** & **CLOSE_TAG:** You can change the open and close tag to indicate the keys
* **LOCALE_FILES_PATH:** Path to locales folder
* **INPUT_FILE_PATH:** Path and filename to input file
* **OUTPUT_FILE_NAME:** Filename to output file

Finally execute the script with:
```bash
python translate.py
```

After running the script you will find a folder for each language file you provided with the translation inside.

##### Example
`ca/index.html`

```html
<li>
  <a href="#services" class="scrollto">Serveis</a>
</li>
<li>
  <a href="#motivation" class="scrollto">Motivació</a>
</li>
<li>
  <a href="#projects" class="scrollto">Projectes</a>
</li>
<li>
  <a href="#team" class="scrollto">Equip</a>
</li>
<li>
  <a href="#contact" class="scrollto">Contacte</a>
</li>
```

For more info you can check the provided example.
