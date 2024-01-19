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

    def agents_setup_tkey(self, agents: "AgentList[Person]"):
        for agent in agents:
            agent.setup_tkey()

