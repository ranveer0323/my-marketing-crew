from crewai import Task


def create_tasks(agents, brand_info):
    brand_name = brand_info.get('brand_name', '')
    industry = brand_info.get('industry', '')
    website = brand_info.get('website', '')
    description = brand_info.get('description', '')
    campaign_goal = brand_info.get('campaign_goal', '')
    brand_document_path = brand_info.get('brand_document_path', None)

    brand_info_text = f"""
    Brand Name: {brand_name}
    Industry: {industry}
    Website: {website}
    Description: {description}
    Campaign Goal: {campaign_goal}
    """

    tasks = [
        Task(
            description=f'1. Analyze the following brand information:\n{brand_info_text}\n'
                        f'2. {"Read and analyze the provided brand document at: " + brand_document_path if brand_document_path else "No brand document provided."}\n'
                        '3. Conduct comprehensive market research to:\n'
                        '   a. Identify 3-5 key customer segments, their behavior and preferences\n'
                        '   b. Analyze how the campaign goal can be achieved for each segment\n'
                        '4. Compile a detailed report that includes:\n'
                        '   a. Brand analysis (industry, purpose, products/services, vision, social media presence)\n'
                        '   b. Customer segment profiles with goal-specific insights\n'
                        '   c. Market trends and competitive analysis focused on similar campaign goals.',
            agent=agents['senior_consultant'],
            expected_output='A comprehensive Brand and Customer Analysis Report in markdown format.',
            output_file='brand_and_customer_analysis.md'
        ),
        Task(
            description='1. Review the Brand and Customer Analysis Report.\n'
                        f'2. Develop a comprehensive marketing strategy aligned with the campaign goal: {campaign_goal}\n'
                        '3. Include in the strategy:\n'
                        '   a. Key objectives and KPIs directly tied to the campaign goal\n'
                        '   b. Platform-specific strategies chosen based on goal effectiveness\n'
                        '   c. Content themes and guidelines that support the campaign goal\n'
                        '4. Ensure the strategy addresses each customer segment and how they relate to achieving the campaign goal.',
            agent=agents['senior_social_media_marketer'],
            expected_output='A detailed Marketing Strategy Report in markdown format.',
            output_file='marketing_strategy.md'
        ),
        Task(
            description='1. Review the Brand Analysis and Marketing Strategy reports.\n'
                        f'2. Create a goal-oriented content plan for the campaign objective: {campaign_goal}\n'
                        '3. Include in the plan:\n'
                        '   a. Two detailed campaign ideas that directly support the goal\n'
                        '   b. A weekly Content calendar with goal-aligned post details\n'
                        '   c. Best timing and frequency for posts to maximize goal achievement\n'
                        '4. Suggest content outline for each post, ensuring alignment with the campaign goal.',
            agent=agents['content_creator'],
            expected_output='A comprehensive Content and Campaign Plan in markdown format.',
            output_file='content_and_campaign_plan.md'
        )
    ]

    return tasks
