from Melodie import Environment
from Melodie import AgentList
from source.person import Person
from source.scenario import DatingScenario


class DatingEnvironment(Environment):
    scenario: "DatingScenario"

    def setup(self):
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0

    def persons_setup_tkey(self, persons: "AgentList[Person]"):
        for person in persons:
            person.setup_tkey()


