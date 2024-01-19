from tab2dict import TabKey
from typing import Optional


class CovidTabKey(TabKey):

    def __init__(
            self,
            id_scenario: Optional[int] = None,
            id_age_group: Optional[int] = None,
            id_health_state: Optional[int] = None
    ):
        self.id_scenario = id_scenario
        self.id_age_group = id_age_group
        self.id_health_state = id_health_state
