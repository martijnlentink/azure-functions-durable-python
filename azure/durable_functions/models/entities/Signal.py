from ..utils.json_utils import add_attrib
from typing import Dict, Union
from ..utils.entity_utils import EntityId


class Signal:
    """An EntitySignal.

    Describes a signal call to a Durable Entity.
    """

    def __init__(self,
                 target: EntityId,
                 name: str,
                 input_: str):
        """Instantiate an EntitySignal.

        Instantiate a signal call to a Durable Entity.

        Parameters
        ----------
        target: EntityId
            The target of signal
        name: str
            The name of the signal
        input_: str
            The signal's input
        """
        self._target = target
        self._name = name
        self._input = input_

    @property
    def target(self) -> EntityId:
        """Get the Signal's target entity.

        Returns
        -------
        EntityId
            EntityId of the target
        """
        return self._target

    @property
    def name(self) -> str:
        """Get the Signal's name.

        Returns
        -------
        str
            The Signal's name
        """
        return self._name

    @property
    def input(self) -> str:
        """Get the Signal's input.

        Returns
        -------
        str
            The Signal's input
        """
        return self._input

    def to_json(self) -> Dict[str, Union[int, str]]:
        """Convert object into a json dictionary.

        Returns
        -------
        Dict[str, Any]
            The instance of the class converted into a json dictionary
        """
        json_dict: Dict[str, Union[int, str]] = {}
        json_dict["target"] = self.target.to_json()
        add_attrib(json_dict, self, 'name')
        add_attrib(json_dict, self, 'input')
        return json_dict
