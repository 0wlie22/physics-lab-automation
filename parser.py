from argparse import ArgumentParser
from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="allow")

    filename: Path
    author: str
    output: Path
    force_overwrite: bool


def parse():
    parser = ArgumentParser()

    parser.add_argument(
        "filename",
        help="file that contains data to process",
        type=Path,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output file name",
        required=False,
    )
    parser.add_argument(
        "-a",
        "--author",
        type=str,
        help="author name",
        required=False,
    )
    parser.add_argument(
        "-f",
        "--force-overwrite",
        help="force overwrite",
        action="store_true",
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="config file",
        required=False,
        default="config.yaml",
    )

    args = vars(parser.parse_args())

    for key in list(args):
        if args[key] is None:
            args.pop(key)

    config_file: dict[str, Any] = {}
    with args["config"].open("r") as f:
        config_file = yaml.safe_load(f)

    settings = Settings(**(config_file | args))

    return settings

print(parse())
