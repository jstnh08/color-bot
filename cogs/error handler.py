import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title=f"Command Error `{ctx.command}`", description=f"{error}", color=discord.Color.red())

        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=f"Command Error `{ctx.command}`", description=f"Missing argument `{error.param.name}`.", color=discord.Color.red())

        else:
            embed = discord.Embed(title="Command Error", description="Unknown error.", color=discord.Color.red())

        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(ErrorHandler(client))

