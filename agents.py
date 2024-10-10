from crewai import Agent
from tools.search_tools import SearchTools
from crewai_tools import FileReadTool


def create_agents(llm):
    file_read_tool = FileReadTool()

    agents = {
        'junior_consultant': Agent(
            role="Junior CRM Data Analyst",
            goal="Analyze customer data from CRM to identify customer segments and behaviors",
            backstory='''You are a skilled data analyst specializing in CRM data analysis. 
            With 5 years of experience, you excel at extracting meaningful insights from customer data, 
            identifying patterns, and creating detailed customer segmentation reports.''',
            verbose=True,
            allow_delegation=False,
            tools=[file_read_tool],
            llm=llm
        ),

        'senior_consultant': Agent(
            role="Senior Marketing Strategy Consultant",
            goal="Analyze brand, CRM insights, and campaign goals to develop targeted, goal-oriented marketing strategies.",
            backstory='''You are a Senior Marketing Strategy Consultant with 15 years of experience in developing 
            goal-oriented marketing campaigns. You excel at analyzing brands, customer data, and crafting strategies 
            that align with specific campaign objectives while understanding market dynamics.''',
            verbose=True,
            allow_delegation=False,
            tools=[file_read_tool, SearchTools.search_internet,
                   SearchTools.search_instagram, SearchTools.search_linkedin],
            llm=llm
        ),

        'senior_social_media_marketer': Agent(
            role="Goal-Oriented Social Media Strategist",
            goal="Develop platform-specific strategies that directly contribute to achieving the campaign's objectives.",
            backstory='''You are an expert in creating targeted social media campaigns that deliver specific outcomes. 
            With over 10 years of experience, you understand how to leverage different platforms to achieve various 
            marketing goals, from brand awareness to lead generation.''',
            verbose=True,
            allow_delegation=True,
            tools=[SearchTools.search_instagram, SearchTools.search_internet],
            llm=llm
        ),

        'content_creator': Agent(
            role="Goal-Driven Content Strategist",
            goal="Create content that directly supports and drives the campaign's objectives across all channels.",
            backstory='''You are a strategic content creator with a proven track record of developing 
            content that achieves specific marketing goals. Your expertise lies in crafting compelling 
            narratives that resonate with target audiences while driving desired outcomes.''',
            verbose=True,
            allow_delegation=False,
            tools=[SearchTools.search_internet],
            llm=llm
        )
    }

    return agents
