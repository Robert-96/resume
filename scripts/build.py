import json

import markdown2
from rost import Rost


def get_context():
    with open("data/data.json") as fp:
        return json.load(fp)


def build(debug=False):
    generator = Rost(
        searchpath="templates",
        outputpath="dist",
        staticpaths=["CNAME", "js", "css", "fonts", "pdf", "img"],
        filters={
            "markdown": lambda x: markdown2.markdown(x)
        },
        contexts=[(".", get_context)],
    )

    if debug:
        generator.watch(monitorpaths=["data/"])
    else:
        generator.build()


if __name__ == "__main__":
    build(debug=True)
