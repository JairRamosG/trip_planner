from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


@CrewBase
class TripPlanner():
    """TripPlanner crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
# --- Agentes ------------------------------------------------------------------
    @agent
    def expert_travel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['expert_travel_agent'],
            tools = [SerperDevTool()],
            verbose=True
        )

    @agent
    def city_selection_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['city_selection_expert'],
            tools = [SerperDevTool()], 
            verbose=True
        )

    @agent
    def local_tour_guide(self) -> Agent:
        return Agent(
            config=self.agents_config['local_tour_guide'],
            tools = [SerperDevTool(), ScrapeWebsiteTool()], 
            verbose=True
        )

# --- Tasks ------------------------------------------------------------------

    @task
    def city_selection(self) -> Task:
        return Task(
            config=self.tasks_config['city_selection'], # type: ignore[index]
        )

    @task
    def gather_city_info(self) -> Task:
        return Task(
            config=self.tasks_config['gather_city_info'], # type: ignore[index]
            output_file='local_guide_report.md'
        )
    
    @task
    def itinerary_planning(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_planning'], # type: ignore[index]
            output_file='itinerary.md'
        )


# --- Crew ------------------------------------------------------------------

    @crew
    def crew(self) -> Crew:
        """Creates the TripPlanner crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
