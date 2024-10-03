from crewai import Agent
from tools.search_tools import SearchTools
from crewai_tools import FileReadTool
from langchain_groq import ChatGroq


def create_agents(llm):
    # Initialize tools
    file_read_tool = FileReadTool()

    agents = {
        'senior_consultant': Agent(
            role="Senior Consultant",
            goal="Analyse the given brand based on the company information to understand the brand's positioning and marketing operations.",
            backstory='''You are a Senior Consultant and specialise in branding and marketing. 
            You analyze the brand based on any provided brand documents and conduct thorough market research. 
            You excel at understanding brand positioning and identifying market opportunities.''',
            verbose=True,
            allow_delegation=False,
            tools=[file_read_tool,
                   SearchTools.search_internet,
                   SearchTools.search_instagram,
                   SearchTools.search_linkedin],
            llm=llm
        ),

        'customer_segment_researcher': Agent(
            role="Customer Segment Researcher",
            goal="Research and understand distinct audience segments, their specific preferences, and behaviors",
            backstory='''You are a veteran market research analyst with 12 years of experience 
            in consumer behavior and market trends. Your expertise lies in conducting comprehensive 
            research to identify and understand different customer segments.''',
            verbose=True,
            allow_delegation=False,
            tools=[SearchTools.search_internet,
                   SearchTools.search_reddit,
                   SearchTools.search_instagram,
                   SearchTools.search_linkedin],
            llm=llm
        ),

        'senior_social_media_marketer': Agent(
            role="Senior Social Media Marketer",
            goal="Develop and implement advanced social media strategies to boost brand awareness, engagement, and conversions across platforms.",
            backstory='''You are a seasoned social media marketing expert with over 10 years of experience 
            in managing high-profile social media campaigns. Your expertise includes crafting compelling 
            content, analyzing trends, and optimizing engagement strategies.''',
            verbose=True,
            allow_delegation=True,
            tools=[SearchTools.search_instagram,
                   SearchTools.search_internet],
            llm=llm
        ),

        'content_creator': Agent(
            role="Creative Content Strategist",
            goal="Generate personalized creative content for each identified audience segment for Instagram and LinkedIn",
            backstory='''You are a former advertising executive, copy writer and content specialist. 
            With 15 years in the industry, you have a deep understanding of brand voice and storytelling 
            techniques across various media.''',
            verbose=True,
            allow_delegation=False,
            tools=[SearchTools.search_internet],
            llm=llm
        )
    }

    return agents
