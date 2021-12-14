import math
from io import BytesIO
from random import randint as rand
import discord
from discord.ext import commands
from converters.colorconverter import ColorConverter
from PIL import Image
from colors import colors


class Color(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colorconverter = ColorConverter()


    def get_closest_match(self, rgb) -> list:
        r1, g1, b1 = rgb

        closest_match = None
        for color, value in colors.items():
            r2, g2, b2 = value
            d = math.sqrt(((r2 - r1) * 0.3) ** 2 + ((g2 - g1) * 0.59) ** 2 + ((b2 - b1) * 0.11) ** 2)
            if closest_match is None: closest_match = (d, color)
            else:
                if closest_match[0] > d:
                    closest_match = (d, color)

        return closest_match

    def display_color_info(self, rgb, hex) -> tuple:
        r, g, b = rgb
        im = Image.new(mode="RGB", size=(200, 200), color=tuple(rgb))
        buffer = BytesIO()
        im.save(buffer, format="PNG")
        buffer.seek(0)
        file = discord.File(buffer, filename="image.png")

        embed = discord.Embed(title=self.get_closest_match(rgb)[1], color=discord.Color.from_rgb(r, g, b))
        embed.add_field(name="RGB", value=", ".join([str(x) for x in rgb]))
        embed.add_field(name="Hex", value=f"#{hex.upper()}")
        embed.set_image(url="attachment://image.png")

        return file, embed

    @commands.command()
    async def getcolor(self, ctx, *, color: ColorConverter) -> discord.Message:
        rgb, hex = color
        file, embed = self.display_color_info(rgb, hex)
        await ctx.reply(file=file, embed=embed)

    @commands.command()
    async def randomcolor(self, ctx) -> discord.Message:
        rgb = [rand(0, 255), rand(0, 255), rand(0, 255)]
        hex = self.colorconverter.rgb_to_hex(rgb)
        file, embed = self.display_color_info(rgb, hex)
        await ctx.reply(file=file, embed=embed)


def setup(client):
    client.add_cog(Color(client))
