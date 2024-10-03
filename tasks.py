from crewai import Task


def create_tasks(agents, brand_info):
    brand_name = brand_info.get('brand_name', '')
    industry = brand_info.get('industry', '')
    website = brand_info.get('website', '')
    description = brand_info.get('description', '')
    brand_document_path = brand_info.get('brand_document_path', None)

    brand_info_text = f"""
    Brand Name: {brand_name}
    Industry: {industry}
    Website: {website}
    Description: {description}
    """

    tasks = [
        Task(
            description=f'1. Analyze the following brand information:\n{brand_info_text}\n'
                        f'2. {"Read and analyze the provided brand document at: " + brand_document_path if brand_document_path else "No brand document provided."}\n'
                        '3. Conduct comprehensive market research to identify 3-5 key customer segments, their behaviour and prefrences.'
                        'Look for and try to find unique and specific insights if possible.'
                        '4. Compile a detailed report that includes:\n'
                        '   a. Brand analysis (industry, purpose, products/services, vision, social media presence)\n'
                        '   b. Customer segment profiles, behaviour and preference analysis and unique insights for each segemnt.\n'
                        '   c. Market trends and competitive analysis.',
            agent=agents['senior_consultant'],
            expected_output='A comprehensive Brand and Customer Analysis Report in markdown format.',
            output_file='brand_and_customer_analysis.md'
        ),
        Task(
            description='1. Review the Brand and Customer Analysis Report.\n'
                        '2. Develop a comprehensive marketing strategy that includes:\n'
                        '   a. Key objectives and KPIs\n'
                        '   b. Platform-specific strategies (Choose the appropriate platforms for the brand.)\n'
                        '   c. Content themes and guidelines\n'
                        'Depending on the brand the strategy can be creative and look unconventional ways to go about their marketing. \n'
                        '3. Ensure the strategy addresses each customer segment, their behavior and preferences and builds on unique insights.',
            agent=agents['senior_social_media_marketer'],
            expected_output='A detailed Marketing Strategy Report in markdown format.',
            output_file='marketing_strategy.md'
        ),
        Task(
            description='1. Review the Brand Analysis and Marketing Strategy reports.\n'
                        '2. Create a comprehensive content plan that includes:\n'
                        '   a. Two detailed campaign ideas\n'
                        '   b. Content calendar with post details for Instagram and LinkedIn\n'
                        '   c. Best timing and frequency for posts\n'
                        '3. Write creative content for each post in the campaign.',
            agent=agents['content_creator'],
            expected_output='A comprehensive Content and Campaign Plan in markdown format.',
            output_file='content_and_campaign_plan.md'
        )
    ]

    return tasks
