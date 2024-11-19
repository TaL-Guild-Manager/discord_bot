# services/discord_poll.py

import discord
from discord import Poll, PollAnswer
from contracts.constants import Constants
from datetime import timedelta

class DiscordPoll:
    def __init__(self, bot):
        self.bot = bot

    async def create_poll(
        self,
        channel_id: int,
        question: str,
        answers: list,
        duration: int,
        multiple: bool = False,
    ):
        channel = self.bot.get_channel(channel_id)
        if not channel:
            raise ValueError("Invalid channel ID provided.")

        if not isinstance(channel, discord.TextChannel):
            raise TypeError("Channel must be a TextChannel to create a poll.")

        if not 1 <= len(answers) <= 20:
            raise ValueError("You must provide between 1 and 20 answers.")

        duration_seconds = self.parse_duration(duration)
        if duration_seconds is None:
            raise ValueError("Invalid duration format. Use '1H', '24H', '3D', or '1W'.")

        poll = Poll(
            question=question[:300],
            duration=timedelta(hours=duration),
            multiple=multiple,
        )

        for answer_text in answers:
            poll.add_answer(text=answer_text[:55])

        poll_message = await channel.send(poll=poll)

        return poll_message 
    
    def parse_duration(self, duration_str):
        duration_str = duration_str.upper()

        return Constants.THREAD_AUTO_ARCHIVE_DURATION.get(duration_str)
