from crewai import Task
from date_utils import get_current_ist_time, get_week_dates, get_optimal_posting_times


def create_tasks(agents, brand_info):
    current_time = get_current_ist_time()
    campaign_start_date = brand_info.get('campaign_start_date')
    week_dates = get_week_dates(campaign_start_date)
    optimal_times = get_optimal_posting_times()

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
    Campaign Start Date: {campaign_start_date}
    Current Date: {current_time.strftime("%Y-%m-%d")}
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
                        '   c. Analysis and effectiveness of similar marketing campaigns by the brand\'s competitors \n'
                        'Use emojis wherever appropriate to make the report look appealing.',
            agent=agents['senior_consultant'],
            expected_output='A comprehensive Brand and Customer Analysis Report in markdown format.',
            output_file='brand_and_customer_analysis.md'
        ),
        Task(
            description='1. Review the Brand and Customer Analysis Report.\n'
                        f'2. Develop a comprehensive marketing strategy aligned with the campaign goal: {campaign_goal}\n'
                        '3. Include in the strategy:\n'
                        '   a. Key objectives and KPIs directly tied to the campaign goal\n'
                        '   b. Platform-specific strategies based on the campaign goal\n'
                        '   c. Content themes and guidelines that support the campaign goal\n'
                        f'4. Create a timeline starting from the campaign start date ({campaign_start_date}) (IST), outlining key milestones and phases\n'
                        '5. Ensure all timing recommendations consider Indian Standard Time (IST) and typical Indian social media usage patterns.'
                        'Use emojis wherever appropriate to make the report look appealing.',
            agent=agents['senior_social_media_marketer'],
            expected_output='A detailed Marketing Strategy Report in markdown format.',
            output_file='marketing_strategy.md'
        ),
        Task(
            description='1. Review the Brand Analysis and Marketing Strategy reports.\n'
                        f'2. Create a goal-oriented content plan for the campaign objective: {campaign_goal}\n'
                        '3. Include in the plan:\n'
                        '   a. Two detailed campaign ideas that directly support the goal\n'
                        f'   b. A weekly content calendar starting from {campaign_start_date} with detailed post schedules\n'
                        '   c. Best posting times based on Indian audience engagement patterns\n'
                        f'4. Use the following week dates for the content calendar:\n{", ".join(week_dates)}\n'
                        '5. Come up with optimal posting times for the seleced social media platforms, account for'
                        f'campaign start date: {campaign_start_date} and the timezone based on this time: {current_time}.'

                        '6. For each post in the calendar, specify:\n'
                        '   - Exact date and time (in IST)\n'
                        '   - Platform\n'
                        '   - Content type and outline\n'
                        '   - Goal alignment\n'
                        f'7. If the campaign start date ({campaign_start_date}) is in the future, include preparation tasks and timelines leading up to the start date.'
                        'Use emojis wherever appropriate to make the report look appealing.',
            agent=agents['content_creator'],
            expected_output='A comprehensive Content and Campaign Plan in markdown format.',
            output_file='content_and_campaign_plan.md'
        )
    ]

    return tasks
