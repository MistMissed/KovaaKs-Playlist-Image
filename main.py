import sys
import os
from PIL import Image, ImageDraw, ImageFont
from playlist import Playlist


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


roboto_bold_path =       resource_path("fonts\\Roboto-Bold.ttf")
roboto_extra_bold_path = resource_path("fonts\\Roboto-ExtraBold.ttf")
roboto_regular_path =    resource_path("fonts\\Roboto-Regular.ttf")

def create_image(playlist: Playlist, outfile: str):
    sharecode_shrink = 0
    if not playlist.share_code.isalpha():
        sharecode_shrink = 45

    # Window
    window_background_color = (143, 141, 144)
    window_margin = 15
    window_radius = 15

    # Playlist Text
    playlist_text_background_color = (106, 106, 108)
    playlist_text_background_height = 90

    playlist_text_color = (154,157,176)
    playlist_text_outline_color = (93,93,94)
    playlist_text_font = ImageFont.truetype(roboto_bold_path, 30)

    # Playlist Name Text
    playlist_name_outline_color = (125,123,127)
    playlist_text_font = ImageFont.truetype(roboto_extra_bold_path, 35)

    # ShareCode area
    sharecode_text_font = ImageFont.truetype(roboto_regular_path, 22)
    sharecode_font = ImageFont.truetype(roboto_extra_bold_path, 23)
    green_box_color = (105,128,97)
    green_box_outline_color = (96,104,83)

    scenarios_box_color = (106,106,108)

    # Scenario Names
    dark_scen_title_background_color = (81, 81, 83)
    scenario_name_height = 37
    scenario_name_font = ImageFont.truetype(roboto_regular_path, 25)

    # Play Count
    play_count_font = ImageFont.truetype(roboto_bold_path, 20)
    play_count_box_color = (165, 164, 164)

    # Find longest text requirement
    playlist_name_length = playlist_text_font.getlength(playlist.playlist_name) + 2 * window_margin + 40
    longest_scenario_name_requirement = 0

    for scenario in playlist.scenario_list:
        current_length = scenario_name_font.getlength(scenario.name)
        if current_length > longest_scenario_name_requirement:
            longest_scenario_name_requirement = current_length

    # Add room for playcount
    longest_scenario_name_requirement += 200

    im_width = int(max(
        playlist_name_length,
        longest_scenario_name_requirement,
        205 + sharecode_font.getlength(playlist.share_code)
    ))

    # add margins
    im_width += (2 * window_margin)

    # Background 
    background_color = (220, 220, 220)
    # im_width = 950
    im_height = 250 + (scenario_name_height * len(playlist.scenario_list)) - sharecode_shrink

    im = Image.new("RGB", (im_width, im_height), background_color)
    d = ImageDraw.Draw(im, "RGB")

    # Window
    d.rounded_rectangle(
        ((window_margin, window_margin), (im_width - window_margin, im_height - window_margin)),
        window_radius,
        window_background_color,
        outline="white",
        width=2
    )

    # Playlist Text
    d.rounded_rectangle(
        (
            (window_margin + 2, window_margin + 2),
            (im_width - window_margin - 2, playlist_text_background_height - window_margin + 5)
        ),
        window_radius,
        playlist_text_background_color,
    )
    d.text(
        (window_margin + 30, window_margin + 17),
        "PLAYLIST",
        font=playlist_text_font,
        fill=playlist_text_color,
        stroke_fill=playlist_text_outline_color,
        stroke_width=1,
    )

    # Playlist Name
    d.text(
        (window_margin + 30, window_margin + 75),
        playlist.playlist_name,
        font=playlist_text_font,
        fill="white",
        stroke_fill=playlist_name_outline_color,
        stroke_width=1
    )

    if playlist.share_code.isalnum():
        # Share Code
        d.text(
            (window_margin + 30, window_margin + 130),
            "Share Code:",
            font=sharecode_text_font,
            fill="white",
            stroke_fill=playlist_name_outline_color,
            stroke_width=1
        )
        d.rounded_rectangle(
            (
                (window_margin + 155, window_margin + 125),
                (window_margin + sharecode_font.getlength(playlist.share_code) + 173, window_margin + 160)
            ),
            radius=1,
            fill=green_box_color,
            width=2,
            outline=green_box_outline_color,
        )
        d.text(
            (window_margin + 165, window_margin + 130),
            playlist.share_code,
            font=sharecode_font,
            fill="white",
            stroke_fill=green_box_outline_color,
            stroke_width=1
        )

    # Scenarios Box
    d.rounded_rectangle(
        (
            (window_margin + 30, window_margin + 167 - sharecode_shrink),
            (im_width - window_margin - 30, im_height - window_margin - 33)
        ),
        15,
        scenarios_box_color,
        outline="white",
        width=2,
    )
    for i, scenario in enumerate(playlist.scenario_list):
        if not i % 2:
            d.rounded_rectangle(
                (
                    (window_margin + 40, 192 - sharecode_shrink + i * scenario_name_height),
                    (im_width - 55, 200 - sharecode_shrink + i * scenario_name_height + 29),
                ),
                radius=15,
                fill=dark_scen_title_background_color,
            )

        d.text(
            (window_margin + 45, 197 - sharecode_shrink + i * scenario_name_height),
            scenario.name,
            font=scenario_name_font,
            fill="white",
            stroke_fill=playlist_name_outline_color,
            stroke_width=1
        )

        # Play Count
        d.rounded_rectangle(
            (
                (im_width - 110, 195 - sharecode_shrink + i * scenario_name_height),
                (im_width - 80, 225 - sharecode_shrink + i * scenario_name_height),
            ),
            fill=None,
            outline=play_count_box_color,
            radius=5,
            width=2
        )
        if scenario.play_count < 10:
            d.text(
                (im_width - 100, 199 - sharecode_shrink + i * scenario_name_height),
                str(scenario.play_count),
                font=play_count_font,
                fill="white",
                stroke_fill=playlist_name_outline_color,

            )
        else:
            d.text(
                (im_width - 106, 199 - sharecode_shrink + i * scenario_name_height),
                str(scenario.play_count),
                font=play_count_font,
                fill="white",
                stroke_fill=playlist_name_outline_color,
            )


    im.save(outfile)

# Testing stuff, multiline comment used to stop it from executing
def test():
    import random
    from scenario import Scenario
    from scenario_generator import generate_random_scenario_name

    global roboto_bold_path
    global roboto_extra_bold_path
    global roboto_regular_path

    roboto_bold_path =       "fonts/Roboto-Bold.ttf"
    roboto_extra_bold_path = "fonts/Roboto-ExtraBold.ttf"
    roboto_regular_path =    "fonts/Roboto-Regular.ttf"

    playlists = (
        Playlist.from_json_file("test_playlists/C - Wednesday - Smooth Tracking (INT) - LG56.json"),
        Playlist.from_json_file("test_playlists/Test Playlist.json"),
        Playlist.from_json_file("test_playlists/cA Static Benchmark Season-1.json"),
        Playlist(
            "",
            "", 
            "Short Name",# "Really Long Test Name For This Stupid Playlist I Guess... FUCK",
            [Scenario(generate_random_scenario_name(), random.randint(1, 10))
                for _ in range(random.randint(1, 7))],
            "KovaaKsBottingShinyDoor"
        ),
        Playlist(
            "",
            "",
            "Air",
            [Scenario("Air", 1)],
            "KovaaKsBottingShinyDoor"
        ),
    )

    playlist = playlists[2]
    create_image(playlist, "output.png")

def main(): 
    playlist_path = sys.argv[1]
    playlist = Playlist.from_json_file(playlist_path)
    outfile = playlist.playlist_name + ".png"
    create_image(playlist, outfile)

if __name__ == "__main__":
    # test()
    main()

