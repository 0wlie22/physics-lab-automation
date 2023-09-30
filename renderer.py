import os
from typing import Any

from jinja2 import Environment, FileSystemLoader


class Renderer:
    def __init__(self, templates_path: str = "templates") -> None:
        self._env = Environment(
            block_start_string="\\BLOCK{",
            block_end_string="}",
            variable_start_string="\\VAR{",
            variable_end_string="}",
            comment_start_string="\\#{",
            comment_end_string="}",
            line_statement_prefix="%-",
            line_comment_prefix="%#",
            autoescape=False,
            loader=FileSystemLoader(os.path.abspath(templates_path)),
        )

    def render(self, template_name: str, args: dict[str, Any]) -> str:
        template = self._env.get_template(template_name)
        return template.render(**args)
