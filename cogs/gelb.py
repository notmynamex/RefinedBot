import requests
import random
import logging
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='--')


def get_gelImage(tags):
    tags = list(tags)
    formatted_tags = ""
    rating = ""
    ratings = {
        "re": "rating%3aexplicit",
        "rq": "rating%3aquestionable",
        "rs": "rating%3asafe"
    }
    if tags:  
        if tags[0] in ratings:
            rating = ratings[tags[0]]
            tags.remove(tags[0])
    if rating == "": 
        rating = ratings["rs"]
    formatted_tags = "_".join(tags).replace("/", "+")
    logging.info(rating, formatted_tags)
    api_url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=50&tags={rating}+{formatted_tags}"
    response = requests.get(api_url)
    try:
        json_api_url = json.loads(response.text)
        image = random.choice(json_api_url)["file_url"]
        return image
    except ValueError:
        return "fucking idiot, that doesnt exist smh, try another tag"

class gelb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command(aliases=["gelb"])
    async def gelbooru(self, ctx, *tags):
        if "loli" in tags:
            logging.info("some lolicon just went to jail")
            return await ctx.send("no lolis you fucking idiot")
        if "rq" in tags or "re" in tags: 
            if ctx.channel.is_nsfw() is True:  
                img = get_gelImage(tags)
                return await ctx.send(img)
            if ctx.channel.is_nsfw() is False:
                return await ctx.send('go to nsfw channel you fuckhead')
        if "rs" in tags:
            img = get_gelImage(tags)
            return await ctx.send(img)


def setup(bot):
    bot.add_cog(gelb(bot))