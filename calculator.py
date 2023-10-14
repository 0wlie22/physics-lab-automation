from parser import Settings
from typing import Self, Union

import numpy as np
import scipy

from renderer import Renderer


class Calculator:
    def __init__(self, author: str):  # noqa: D107
        self.author = author

    @classmethod
    def from_config(cls, config: Settings) -> Self:
        """Creates calculator from config.

        Args:
            config (BaseSettings): config.

        Returns:
            Calculator: calculator.
        """
        return cls(author=config.author)

    def calculate(self, data: list[float]) -> Self:
        return self

    def get_student_coef(count: Union[int, np.Inf], probability: float = 0.95) -> float:
        """Get student coefficient for specified measurement count and confidence probability.

        Args:
            count (int | numpy.Inf): measurement count.
            probability (float): confidence probability.

        Returns:
            float: student coefficient.
        """
        return scipy.stats.t.ppf((1 + probability) / 2, count - 1)

    def render(self) -> str:
        return Renderer().render("template.md")
