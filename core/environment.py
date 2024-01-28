import random

from Melodie import AgentList
from Melodie import Environment

from core.person import Person
from core.scenario import DatingScenario
from utils.funcs import dict_sample


class DatingEnvironment(Environment):
    scenario: "DatingScenario"

    def setup(self):
        self.total_assessment = 0
        self.dates = []

    @staticmethod
    def persons_setup_data(persons: "AgentList[Person]"):
        for person in persons:
            person.setup_tkey()
            person.setup_age()

    @staticmethod
    def persons_get_income(persons: "AgentList[Person]"):
        for person in persons:
            person.get_income()

    @staticmethod
    def persons_spend_income(persons: "AgentList[Person]"):
        for person in persons:
            person.spend_income()

    def sample_candidates(self, persons: "AgentList[Person]"):
        total_social = 0
        for person in persons:
            total_social += person.social
        return random.choices(
            persons,
            weights=[person.social/total_social for person in persons],
            k=self.scenario.candidate_num
        )

    def organize_dates(self, potential_selectors: "AgentList[Person]", potential_candidates: "AgentList[Person]", period: int):
        selectors = potential_selectors.random_sample(self.scenario.selector_num)
        for selector in selectors:
            candidates = self.sample_candidates(potential_candidates)
            d = {}
            for index, candidate in enumerate(candidates):
                assessment = selector.assess_candidate(
                    candidate_age=candidate.age,
                    candidate_saving=candidate.saving
                )
                d[index] = assessment if assessment > 0 else 0
            selected_candidate = candidates[dict_sample(d)]
            assessment = selector.assess_candidate(
                    candidate_age=selected_candidate.age,
                    candidate_saving=selected_candidate.saving
                )
            self.dates.append({
                "id_scenario": self.scenario.id,
                "id_run": self.scenario.id_run,
                "period": period,
                "selector_id": selector.id,
                "selector_id_gender": selector.tkey.id_gender,
                "selector_id_age_group": selector.tkey.id_age_group,
                "selector_id_income_group": selector.tkey.id_income_group,
                "selector_age": selector.age,
                "selector_income": selector.income,
                "selector_social": selector.social,
                "selector_saving": selector.saving,
                "selector_weight_age": selector.weight_age,
                "selector_weight_saving": selector.weight_saving,
                "candidate_id": selected_candidate.id,
                "candidate_id_gender": selected_candidate.tkey.id_gender,
                "candidate_id_age_group": selected_candidate.tkey.id_age_group,
                "candidate_id_income_group": selected_candidate.tkey.id_income_group,
                "candidate_age": selected_candidate.age,
                "candidate_income": selected_candidate.income,
                "candidate_social": selected_candidate.social,
                "candidate_saving": selected_candidate.saving,
                "assessment": assessment
            })
            self.total_assessment += assessment

    def reset_total_assessment(self):
        self.total_assessment = 0
