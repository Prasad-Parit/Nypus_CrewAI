from textwrap import dedent
from crewai import Task

class ContentCreationTasks:


     def coordination_task(self, agent, tasks_results, overall_strategy):
        return Task(
            description=dedent(f"""\
                Review and coordinate the outputs from all tasks to ensure alignment 
                with the marketing strategy. Provide feedback for improvements if needed.

                Tasks Results: {tasks_results}
                Overall Strategy: {overall_strategy}"""),
            expected_output=dedent("""\
                A finalized set of cohesive content assets ready for deployment."""),
            async_execution=False,
            agent=agent
        )


    def trend_research_task(self, agent, target_audience, industry_context):
        return Task(
            description=dedent(f"""\
                Research current industry trends and audience interests to identify
                potential topics for blog posts. Analyze market data, competitor content, 
                and emerging trends to curate ideas that align with the target audience 
                and industry context.

                Target Audience: {target_audience}
                Industry Context: {industry_context}"""),
            expected_output=dedent("""\
                A curated list of 10-15 trending blog post ideas based on audience 
                interests and industry trends."""),
            async_execution=True,
            agent=agent
        )

    def seo_content_task(self, agent, keywords, content_context):
        return Task(
            description=dedent(f"""\
                Create engaging SEO-optimized articles by incorporating the provided 
                keywords and adhering to SEO best practices. Focus on delivering 
                valuable content that aligns with the provided context.

                Keywords: {keywords}
                Content Context: {content_context}"""),
            expected_output=dedent("""\
                SEO-optimized articles ready for publication, complete with meta 
                descriptions, headings, and keywords strategically placed."""),
            async_execution=True,
            agent=agent
        )

   
    def social_media_task(self, agent, platforms, campaign_context):
        return Task(
            description=dedent(f"""\
                Develop engaging and platform-specific social media posts tailored 
                for the provided platforms. Align the posts with the ongoing campaign 
                context and audience preferences.

                Platforms: {platforms}
                Campaign Context: {campaign_context}"""),
            expected_output=dedent("""\
                A set of 5-10 tailored social media posts for each platform, including 
                captions and visuals ready for scheduling."""),
            async_execution=False,
            agent=agent
        )


    def email_marketing_task(self, agent, target_audience, product_updates):
        return Task(
            description=dedent(f"""\
                Design and create engaging email campaigns to inform subscribers 
                about the latest product updates, promotions, and company news. 

                Target Audience: {target_audience}
                Product Updates: {product_updates}"""),
            expected_output=dedent("""\
                A complete email newsletter template ready for distribution, with 
                attention-grabbing subject lines and actionable CTAs."""),
            async_execution=False,
            agent=agent
        )

    def product_description_task(self, agent, product_list, tone_of_voice):
        return Task(
            description=dedent(f"""\
                Write compelling and informative product descriptions for the provided 
                list of products. Ensure the descriptions align with the specified 
                tone of voice and emphasize features and benefits.

                Product List: {product_list}
                Tone of Voice: {tone_of_voice}"""),
            expected_output=dedent("""\
                A collection of well-crafted product descriptions ready for an 
                e-commerce website."""),
            async_execution=True,
            agent=agent
        )


    def video_script_task(self, agent, video_purpose, audience_demographics):
        return Task(
            description=dedent(f"""\
                Develop detailed scripts for promotional videos that clearly convey 
                the intended message. Focus on engaging the target audience while 
                including call-to-action elements.

                Video Purpose: {video_purpose}
                Audience Demographics: {audience_demographics}"""),
            expected_output=dedent("""\
                Completed video scripts ready for production, including scene-by-scene 
                breakdowns and dialogue."""),
            async_execution=True,
            agent=agent
        )

  
    def infographic_design_task(self, agent, data_points, infographic_context):
        return Task(
            description=dedent(f"""\
                Design visually appealing infographics that represent the provided 
                data points effectively. Ensure the design aligns with the infographic 
                context and simplifies complex information.

                Data Points: {data_points}
                Infographic Context: {infographic_context}"""),
            expected_output=dedent("""\
                High-quality infographics ready for publication, showcasing the 
                data in an engaging and digestible format."""),
            async_execution=True,
            agent=agent
        )


    def proofreading_task(self, agent, draft_content, content_context):
        return Task(
            description=dedent(f"""\
                Edit and proofread the provided draft content to ensure grammatical 
                accuracy, clarity, and consistency. Align the final content with the 
                specified context.

                Draft Content: {draft_content}
                Content Context: {content_context}"""),
            expected_output=dedent("""\
                Polished versions of the content, free of errors and aligned with 
                the overall strategy."""),
            async_execution=False,
            agent=agent
        )

 
   