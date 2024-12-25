import json
import sys


def if_values(test_data):
    if test_data.get("values"):
        return True
    else:
        return False


def set_value(test_data):
    for d in test_data:
        if d.get("value") == "":
            with open(sys.argv[1], "r", encoding="utf-8") as values:
                values_data = json.loads(values.read())
                for i in values_data["values"]:
                    if i["id"] == d["id"]:
                        d["value"] = i["value"]
        if if_values(d):
            set_value(d["values"])


if __name__ == "__main__":
    with open(sys.argv[2], "r", encoding="utf-8") as tests:
        test_data = json.loads(tests.read())

    set_value(test_data["tests"])

    with open(sys.argv[3], "w", encoding="utf-8") as report:
        json_str = json.dumps(test_data, indent=2)
        report.write(json_str)
