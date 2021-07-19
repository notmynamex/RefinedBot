import logging
from discord.ext import tasks, commands
import datetime
from firebase_admin import firestore
import pytz

db = firestore.client()
jst = pytz.timezone("Japan")

class reminder2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=1)
    async def times(self):
        await self.bot.wait_until_ready()
        data = db.collection('Reminders').document('Reminder-Times').get().get('Times')
        now = datetime.datetime.now(tz=jst).strftime('%H-%M')
        for time in data:
            if (str(time['time']) == str(now)):
                logging.info(f"Reminding {time['mention']} about {time['title']}")
                await self.bot.get_channel(id=756181136337797270).send(f"<@{time['mention']}> Reminder: `{time['title']}`")
    @commands.Cog.listener()
    async def on_ready(self):
        self.times.start()


def setup(bot):
    bot.add_cog(reminder2(bot))