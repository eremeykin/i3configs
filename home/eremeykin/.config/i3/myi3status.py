import sys
import json
import subprocess

FILLED_SYMB='▰'
EMPTY_SYMB='▱'

def _get_by_name(source_json, name):
    for entry in source_json:
        if entry["name"] == name:
            return entry

def _append_redshift(json_raw):
    with open('/home/eremeykin/.config/i3/redshift/status.rsh', 'r') as json_file:
        data = json.load(json_file)
    json_raw.insert(0, data)

def _add_brightness(json_raw):
    current_brightness=float(subprocess.check_output(['xbacklight', '-get']))
    filled=int(current_brightness//10)
    text=FILLED_SYMB*filled+EMPTY_SYMB*(10-filled)
    brightness_json = { "name": "brightness", "markup": "none" }
    brightness_json["full_text"]=text +  '{:3d}'.format(int(current_brightness)) + "%"
    json_raw.insert(0, brightness_json)


def main(source_json):
    json_raw = json.loads(source_json)
    volume = _get_by_name(json_raw, "volume")
    _append_redshift(json_raw)
    _add_brightness(json_raw)
    return json.dumps(json_raw)

if __name__ == '__main__':
    input = sys.argv[1]
    if input.startswith(','):
        input=input[1:]
        print(","+main(input))
    else:
        print(False)
        print(main(input))
