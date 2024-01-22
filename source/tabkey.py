from tab2dict import TabKey
from typing import Optional


class DatingTabKey(TabKey):

    def __init__(
            self,
            id_gender: Optional[int] = None,
            id_state: Optional[int] = None,
            id_age_group: Optional[int] = None,
            id_income_group: Optional[int] = None
    ):
        self.id_gender = id_gender
        self.id_state = id_state
        self.id_age_group = id_age_group
        self.id_income_group = id_income_group
