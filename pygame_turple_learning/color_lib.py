mod_color = []
colors = [
    "#FF0000",  # red
    "#0000FF",  # blue
    "#008000",  # green
    "#FFFF00",  # yellow
    "#800080",  # purple
    "#FFA500",  # orange
    "#000000",  # black
    "#808080",  # gray
    "#DC143C",  # crimson
    "#40E0D0",  # turquoise
    "#36454F",  # charcoal
    "#FFBF00",  # amber
    "#4B0082",  # indigo
    "#00A86B",  # jade
    "#007BA7",  # cerulean
    "#FF00FF",  # magenta
    "#FA8072",  # salmon
    "#E6E6FA",  # lavender
    "#E0B0FF",  # mauve
    "#F4C430",  # saffron

    # added shades/tints
    "#B22222",  # firebrick (dark red)
    "#1E90FF",  # dodger blue
    "#006400",  # dark green
    "#FFD700",  # gold
    "#BA55D3",  # medium orchid
    "#FF8C00",  # dark orange
    "#A9A9A9",  # dark gray
    "#2F4F4F",  # dark slate gray
    "#8B0000",  # dark red
    "#20B2AA",  # light sea green
    "#708090",  # slate gray
    "#DAA520",  # goldenrod
    "#6A5ACD",  # slate blue
    "#50C878",  # emerald
    "#4682B4",  # steel blue
    "#C71585",  # medium violet red
    "#CD5C5C",  # indian red
    "#D8BFD8",  # thistle
    "#DDA0DD",  # plum
    "#FFDAB9"   # peach puff
]


def hex_to_rgb(hex_string):
    hex_string = hex_string.lstrip("#")
    r_hex = hex_string[0:2]
    g_hex = hex_string[2:4]
    b_hex = hex_string[4:6]
    return [int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)]


def too_close(ref_hex, scaned_hex, to_close):
    R = True
    G = True
    B = True
    ref_rgb = hex_to_rgb(ref_hex)
    scanned_rgb = hex_to_rgb(scaned_hex)
    if abs(ref_rgb[0] - scanned_rgb[0]) <= to_close:
        R = False
    if abs(ref_rgb[1] - scanned_rgb[1]) <= to_close:
        G = False
    if abs(ref_rgb[2] - scanned_rgb[2]) <= to_close:
        B = False
    if (R == False and G == False and B == False):
        return False


def make_mod_color(ref_hex, to_close):
    for item in colors:
        keep = too_close(ref_hex, item, to_close)
        if not keep == False:
            mod_color.append(str(item))
