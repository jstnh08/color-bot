import discord
from discord.ext import commands


class ColorConverter(commands.Converter):
    def __init__(self):
        self.hex_convert = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        self.rgb_convert = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

    def hex_to_rgb(self, hex_value) -> list:
        base = list(zip(list(hex_value)[::2], list(hex_value)[1::2]))
        rgb = []
        for pair in base:
            converted = 0
            for i, char in enumerate(pair):
                if char not in self.hex_convert and not char.isdigit():
                    raise commands.BadArgument(message="That isn't a valid color! It needs to be either RGB or Hex!")
                else:
                    converted += (((1 - i) * 15) + 1) * (self.hex_convert[char] if not char.isdigit() else int(char))

            rgb.append(converted)

        return rgb

    def arg_to_rgb(self, argument) -> list:
        rgb = argument.replace(",", " ").split(" ")
        for x in rgb.copy():
            if x == "": rgb.remove(x)
        if len(rgb) != 3:
            raise commands.BadArgument(message="That isn't a valid color! It needs to be either RGB or Hex!")
        for i, color in enumerate([x.strip() for x in rgb]):
            if not color.isdigit():
                raise commands.BadArgument(message="That isn't a valid color! It needs to be either RGB or Hex!")
            rgb[i] = int(color)
        for x in rgb:
            if 0 > x or x > 255:
                raise commands.BadArgument(message="That isn't a valid color! All RGB values need to be between 0-255!")
        return rgb

    def rgb_to_hex(self, rgb) -> str:
        hex = ""
        for x in rgb:
            hex += f"{x//16 if len(str(x//16))==1 else self.rgb_convert[x//16]}{x%16 if len(str(x%16))==1 else self.rgb_convert[x%16]}"
        return hex

    async def convert(self, ctx, argument) -> tuple:
        argument = argument.lower()
        if argument[0] == "#": argument = argument.strip("#")
        if len(argument) == 6 and " " not in argument and "," not in argument:
            rgb = self.hex_to_rgb(argument)
        else:
            rgb = self.arg_to_rgb(argument)
        return rgb, self.rgb_to_hex(rgb)