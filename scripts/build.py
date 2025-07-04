import json
import logging

import markdown2
from rost import Rost

from .config import CONFIG

logger = logging.getLogger(__name__)


def get_context():
    """Load the main context from the data file."""

    with open(CONFIG.data_path) as fp:
        return json.load(fp)


def get_overwrite_context():
    """Load the overwrite context from the overwrite file."""

    if not CONFIG.overwrites_path.exists():
        return {}

    with open(CONFIG.overwrites_path) as fp:
        return json.load(fp)


def apply_overwrite(context):
    """Apply the overwrite context to the main context."""

    if CONFIG.disable_overwrites:
        logger.info("Overwrites are disabled. Skipping context overwrite.")
        return context

    overwrite = get_overwrite_context()

    if not overwrite:
        return context

    for key, value in overwrite.items():
        if isinstance(value, list):
            continue  # Skip lists as they are not merged

        # If the value is not a dict, we replace it directly
        if not isinstance(value, dict):
            context[key] = value
            continue

        # If the value is a dict, we merge it with the existing context
        if key not in context:
            context[key] = value
            continue

        if not isinstance(context[key], dict):
            value_type = type(context[key]).__name__
            raise TypeError(
                f"Cannot merge dictionaries for key '{key}': "
                f"the original context contains a value of type {value_type}, "
                f"but the overwrite file provides a dictionary. "
                "Please ensure both values are dictionaries to allow merging."
            )

        context[key].update(value)

    return context


def build(debug=False):
    generator = Rost(
        searchpath="templates",
        outputpath="dist",
        staticpaths=["CNAME", "js", "css", "fonts", "pdf", "img"],
        filters={
            "markdown": lambda x: markdown2.markdown(x)
        },
        contexts=[(".", lambda: apply_overwrite(get_context()))],
    )

    if debug:
        generator.watch(monitorpaths=["data/"])
    else:
        generator.build()


if __name__ == "__main__":
    build(debug=True)
