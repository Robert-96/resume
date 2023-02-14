import json

from rost import Rost


def get_context():
    with open("data/data.json") as fp:
        return json.load(fp)


def build(debug=False):
    generator = Rost(
        searchpath="templates",
        outputpath="dist",
        staticpaths=["CNAME", "css", "fonts"],
        contexts=[
            ('.', get_context)
        ],
    )

    if debug:
        generator.watch(monitorpaths=["data/"])
    else:
        generator.build()


if __name__ == "__main__":
    build(debug=True)
