from typing import TYPE_CHECKING

from Melodie import Agent

if TYPE_CHECKING:
    from source.scenario import DatingScenario


class Person(Agent):
    scenario: "DatingScenario"

    def setup(self):
        self.id_gender: int = 0
        self.id_state: int = 0
        self.threshold: float = 0.0
        self.share_social: float = 0.0
        self.share_saving: float = 0.0
        self.share_quality: float = 0.0
        self.weight_age: float = 0.0
        self.weight_saving: float = 0.0
        self.weight_quality: float = 0.0
        self.age: int = 0
        self.saving: float = 0.0
        self.quality: float = 0.0
