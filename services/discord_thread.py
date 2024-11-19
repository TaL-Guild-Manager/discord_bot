# services/discord_thread.py

import discord

from contracts.constants import Constants

class DiscordThread:
    def __init__(self, bot):
        self.bot = bot

    async def create_thread(
        self,
        channel_id,
        thread_name,
        message_content=None,
        auto_archive_duration=Constants.THREAD_AUTO_ARCHIVE_DURATION['1W'],
        applied_tags=Constants.FORUM_TAGS['Raid'],
    ):
        channel = self.bot.get_channel(channel_id)

        if not isinstance(channel, discord.ForumChannel):
            raise TypeError("Channel must be a ForumChannel to create a forum thread.")
        
        if isinstance(auto_archive_duration, str):
            auto_archive_duration = Constants.THREAD_AUTO_ARCHIVE_DURATION.get(auto_archive_duration.upper(), 10080)
            print(f"Auto-archive duration set to {auto_archive_duration} minutes.")
        
        if isinstance(applied_tags, str):
            tag_names = [tag.strip() for tag in applied_tags.split(',')]
            available_tags = {tag.name: tag for tag in channel.available_tags}
            tag_objects = []
            for tag_name in tag_names:
                tag = available_tags.get(tag_name)
                if tag:
                    tag_objects.append(tag)
                else:
                    raise ValueError(f"Unknown tag name: '{tag_name}'")
            applied_tags = tag_objects

        print(f"Applied tags: {applied_tags}")

        thread_with_message = await channel.create_thread(
            name=thread_name,
            content=message_content,
            auto_archive_duration=auto_archive_duration,
            applied_tags=applied_tags
        )

        thread = thread_with_message.thread
        
        return thread
