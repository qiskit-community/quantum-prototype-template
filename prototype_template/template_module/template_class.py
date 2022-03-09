"""Template class."""

from typing import Union, List, Optional


class TemplateClass:
    """Template class for demo purposes."""

    def __init__(
        self,
        some_parameter: Union[
            int, float, str, bool, List[Union[int, float, str, bool]]
        ],
        optional_parameter: Optional[
            Union[int, float, str, bool, List[Union[int, float, str, bool]]]
        ] = None,
    ):
        """TemplateClass

        Args:
            some_parameter: some parameter for class
            optional_parameter: some optional parameter for class
        """
        self._some_parameter = some_parameter
        self._optional_parameter = optional_parameter

    def __repr__(self):
        return f"TemplateClass({self._some_parameter})"

    def multiply(
        self, parameter: int
    ) -> Union[int, float, str, bool, List[Union[int, float, str, bool]]]:
        """Return `parameter` multiplied by `some_parameter`.

        Args:
            parameter: parameter description

        Returns:
            `parameter` input multiplied by `some_parameter`

        Example:
            >>> from prototype_template import TemplateClass
            >>> t = TemplateClass(some_parameter=3)
            >>> t.multiply(2)
            6
        """
        return parameter * self._some_parameter
