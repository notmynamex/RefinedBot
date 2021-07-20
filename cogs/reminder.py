import logging
from discord.ext import tasks, commands
import datetime
from firebase_admin import firestore

db = firestore.client()

class reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @tasks.loop(minutes=1)
    async def reminders(self):
        await self.bot.wait_until_ready()
        data = db.collection('Reminders').document('Reminders').get().get('Reminders')
        now = datetime.datetime.now(tz=datetime.timezone.utc).strftime('%d-%m-%Y-%H-%M')
        for reminder in data:
            if (str(reminder['time']) == str(now)):
                logging.info(f"Reminding {reminder['mention']} about {reminder['title']}")
                await self.bot.get_channel(id={reminder['channel_id']}).send(f"<@{reminder['mention']}> Reminder: `{reminder['title']}`")
    @commands.Cog.listener()
    async def on_ready(self):
        self.reminders.start()


def setup(bot):
    bot.add_cog(reminder(bot))