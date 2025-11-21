import json
from dataclasses import dataclass
from scenario import Scenario

@dataclass
class Playlist:
    author_name: str
    description: str
    playlist_name: str
    scenario_list: list[Scenario]
    share_code: str

    @staticmethod
    def from_json_file(file_name):
        with open(file_name, "r") as f:
             playlist_data = json.load(f)

        author_name = playlist_data["authorName"]
        description = playlist_data["description"]
        playlist_name = playlist_data["playlistName"]
        share_code = playlist_data["shareCode"]
        scenario_list = []

        for scenario in playlist_data["scenarioList"]:
            scenario_name, play_count = scenario.values()
            scenario_list.append(Scenario(scenario_name, play_count))

        return Playlist(
            author_name,
            description,
            playlist_name,
            scenario_list,
            share_code
        )


if __name__ == "__main__":
    TEST_FILE = "C - Wednesday - Smooth Tracking (INT) - LG56.json"
    test_playlist = Playlist.from_json_file(TEST_FILE)
    for scenario in test_playlist.scenario_list:
        print("\t", scenario)


