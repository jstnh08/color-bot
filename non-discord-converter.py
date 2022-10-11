class ColorConverter:
    def __init__(self):
        pass
    
    def hex_to_rgb(self, hex: str) -> list:        
        hex = [list(x) for x in zip(hex.lower()[::2], hex.lower()[1::2])]
        
        for x in hex:
            for i, y in enumerate(x):
                x[i] = (int(y) if y.isdigit() else ord(y)-87)*[16, 1][i]

       return [sum(x) for x in hex]
        
    def rgb_to_hex(self, rgb: list) -> str:
        def letter(x):
            return str(x) if x < 10 else chr(87+x)
            
        hex = ""
        for x in rgb:
            hex += letter(x//16)+letter(x%16)

       return hex

cc = ColorConverter()

if __name__ == '__main__':
    print(cc.rgb_to_hex([255, 174, 255]))
