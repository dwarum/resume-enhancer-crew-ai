from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ATSCheckCrew():
    """ATSCheck crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks_ats.yaml'

    @agent
    def ats_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['ats_checker'], # type: ignore[index]
            verbose=True
        )

    @task
    def check_ats_compatibility(self) -> Task:
        return Task(
            config=self.tasks_config['check_ats_compatibility'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ATSCheck crew"""
        return Crew(
            agents=[self.ats_checker()],
            tasks=[self.check_ats_compatibility()],
            process=Process.sequential,
            verbose=True
        )
    
@CrewBase
class ResumeEnhancerCrew():
    """ResumeEnhancer crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks_enhancer.yaml'

    @agent
    def resume_enhancer_initial(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_enhancer_initial'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def resume_enhancer_final(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_enhancer_final'], # type: ignore[index]
            verbose=True
        )

    @task
    def enhance_resume_initial(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_resume_initial'], # type: ignore[index]
        )
    
    @task
    def enhance_resume_final(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_resume_final'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeEnhancer crew"""
        return Crew(
            agents=[self.resume_enhancer_initial(), self.resume_enhancer_final()],
            tasks=[self.enhance_resume_initial(), self.enhance_resume_final()],
            process=Process.sequential,
            verbose=True,
        )

