from typing import TYPE_CHECKING

from Melodie import Agent

from source.tabkey import DatingTabKey
from source.utils import dict_sample

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
        self.saving: float = 0.0
        self.quality: float = 0.0

    def setup_tkey(self):
        self.tkey = DatingTabKey(
            id_gender=self.id_gender,
            id_state=self.id_state
        )
        self.tkey.id_age_group = self.setup_id_age_group()
        self.tkey.id_income_group = self.setup_id_income_group()

    def setup_id_age_group(self):
        d = {}
        for id_age_group in range(1, len(self.scenario.age_groups) + 1):
            self.tkey.id_age_group = id_age_group
            d[id_age_group] = self.scenario.prob_age_group.get_item(self.tkey)
        return dict_sample(d)

    def setup_id_income_group(self):
        d = {}
        l = self.scenario.rel_age_group_income_group.get_item(self.tkey)
        for id_income_group in l:
            self.tkey.id_income_group = id_income_group
            d[id_income_group] = self.scenario.prob_income_group.get_item(self.tkey)
        return dict_sample(d)
