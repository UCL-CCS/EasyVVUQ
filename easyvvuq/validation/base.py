from easyvvuq.base_element import BaseElement
import logging

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class BaseValidationElement(BaseElement):
    """Baseclass for all EasyVVUQ validation element.

    Attributes
    ----------
    validation_name : str
        Name of the particular Validation Element.

    """

    def __init_subclass__(cls, validation_name, **kwargs):
        """
        Catch any new validation elements (all elements must inherit from
        BaseValidationElement) and add them to the dict of available elements.

        Parameters
        ----------
        validation_name : str
            Name of the particular validation element.
        """

        super().__init_subclass__(**kwargs)

        cls.validation_name = validation_name

        # Register new validation element
        AVAILABLE_VALIDATION_ELEMENTS[validation_name] = cls

    def element_category(self):
        return "validation_element"

    def element_name(self):
        return self.validation_name

    def element_version(self):
        raise NotImplementedError

    def is_finite(self):
        raise NotImplementedError


    @staticmethod
    def deserialize(serialized_validation_element):
        """Deserialize a validation element.

        Parameters
        ----------
        serialized_validation_element : str
            Validation element serialized in JSON format.

        Returns
        -------

        """

        inputs = json.loads(serialized_validation_element)

        if not inputs["restartable"]:
            msg = f'Validation {inputs["element_name"]} is not restartable'
            logging.error(msg)
            raise Exception(msg)

        if 'vary' in inputs["state"]:
            inputs["state"]["vary"] = Vary.deserialize(inputs["state"]["vary"]).vary_dict

        validation_element = AVAILABLE_VALIDATION_ELEMENTS[inputs["element_name"]](**inputs["state"])
        return validation_element
