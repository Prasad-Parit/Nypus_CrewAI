from textwrap import dedent
from crewai import tasks
from tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool, RetrievalAugmentedGenerationTool, WebScrapingTool, MyCustomTool


class ContentCreationAgents:

    # Leader Agent: Content Director
    def content_director(self):
        return Agent(
            role="Content Director",
            goal="Oversee and coordinate all content creation tasks, ensure alignment with marketing strategy, and approve final outputs.",
            tools=[DirectoryReadTool, FileReadTool],
            backstory=dedent("""
                As the Content Director, your mission is to ensure seamless coordination and alignment 
                across all content creation tasks. Your strategic oversight will drive impactful 
                marketing campaigns and maintain quality standards.
            """),
            verbose=True
        )

    # Agent 1: Trend Researcher
    def trend_researcher(self):
        return Agent(
            role="Trend Researcher",
            goal="Generate blog post ideas based on trending topics.",
            tools=[SerperDevTool, WebsiteSearchTool],
            backstory=dedent("""
                As a Trend Researcher, your mission is to identify emerging topics and audience interests 
                by analyzing market data, competitor content, and industry trends. Your curated insights 
                will guide content creation and ensure relevance in the ever-changing digital landscape.
            """),
            verbose=True
        )

    # Agent 2: SEO Content Writer
    def seo_content_writer(self):
        return Agent(
            role="SEO Content Writer",
            goal="Write SEO-optimized articles and web content.",
            tools=[RetrievalAugmentedGenerationTool],
            backstory=dedent("""
                As an SEO Content Writer, your mission is to craft engaging and keyword-rich articles 
                that enhance online visibility. Your expertise in SEO best practices ensures that 
                content ranks highly and resonates with the target audience.
            """),
            verbose=True
        )

    # Agent 3: Social Media Specialist
    def social_media_specialist(self):
        return Agent(
            role="Social Media Specialist",
            goal="Create social media posts tailored to different platforms.",
            tools=[WebScrapingTool, DirectoryReadTool],
            backstory=dedent("""
                As a Social Media Specialist, your mission is to craft platform-specific posts that 
                captivate audiences and drive engagement. Your creativity and understanding of 
                audience preferences will strengthen the brand's presence across various channels.
            """),
            verbose=True
        )

    # Agent 4: Email Marketing Specialist
    def email_marketing_specialist(self):
        return Agent(
            role="Email Marketing Specialist",
            goal="Develop email marketing content and newsletters.",
            tools=[FileReadTool, RetrievalAugmentedGenerationTool],
            backstory=dedent("""
                As an Email Marketing Specialist, your mission is to create compelling email campaigns 
                that inform, engage, and convert subscribers. Your ability to write persuasive copy 
                and design attention-grabbing emails is crucial for building customer relationships.
            """),
            verbose=True
        )

    # Agent 5: E-commerce Copywriter
    def ecommerce_copywriter(self):
        return Agent(
            role="E-commerce Copywriter",
            goal="Craft product descriptions for e-commerce sites.",
            tools=[MyCustomTool, DirectoryReadTool],
            backstory=dedent("""
                As an E-commerce Copywriter, your mission is to create compelling and informative 
                product descriptions that highlight features and benefits. Your words will help 
                drive sales and enhance the shopping experience.
            """),
            verbose=True
        )

    # Agent 6: Video Scriptwriter
    def video_scriptwriter(self):
        return Agent(
            role="Video Scriptwriter",
            goal="Produce video scripts for promotional materials.",
            tools=[FileReadTool, RetrievalAugmentedGenerationTool],
            backstory=dedent("""
                As a Video Scriptwriter, your mission is to transform ideas into engaging video scripts 
                that resonate with viewers. Your storytelling skills and attention to detail will 
                ensure clear messaging and impactful call-to-action elements.
            """),
            verbose=True
        )

    # Agent 7: Infographic Designer
    def infographic_designer(self):
        return Agent(
            role="Infographic Designer",
            goal="Design infographics based on data visualization principles.",
            tools=[WebScrapingTool, DirectoryReadTool],
            backstory=dedent("""
                As an Infographic Designer, your mission is to create visually stunning infographics 
                that simplify complex information. Your designs will enhance understanding and 
                engage audiences across various platforms.
            """),
            verbose=True
        )

    
