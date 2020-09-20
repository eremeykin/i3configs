import sys
import json

def _get_by_name(source_json, name):
    for entry in source_json:
        if entry["name"] == name:
            return entry

def _append_redshift(json_raw):
    with open('/home/eremeykin/.config/i3/redshift/status.rsh', 'r') as json_file:
        data = json.load(json_file)
    json_raw.insert(0, data)


def main(source_json):
    json_raw = json.loads(source_json)
    volume = _get_by_name(json_raw, "volume")
    _append_redshift(json_raw)
    return json.dumps(json_raw)

if __name__ == '__main__':
    input = sys.argv[1]
    if input.startswith(','):
        input=input[1:]
        print(","+main(input))
    else:
        print(False)
        print(main(input))
