from typing import List, Dict

from bases import Bases
from player import Player


if __name__ == "__main__":
    player_1 = Player(name="red")
    player_2 = Player(name="blue")

    innings: int = 9
    MAX_OUTS: int = 3
    team_turns: List[Player] = [player_1 if i % 2 == 0 else player_2 for i in range(innings)]
    rules: Dict[int, str] = {1: "1st base", 2: "2nd base", 3: "3rd base", 4: "Home Run"}
    
    current_game = Bases()
    for current_team in team_turns:
        print(f"--- TEAM {current_team.name} is at bat ---")
        current_outs: int = 0

        while current_outs < MAX_OUTS:
            # Batter get a hit
            batter_hit = current_game.calculate_new_runs()
            print(f"TEAM {current_team.name} hit {rules.get(batter_hit, "OUT")} ({batter_hit})")

            if batter_hit >= 5:
                current_outs += 1
                if current_outs == MAX_OUTS:
                    print(f"TEAM {current_team.name} have 3 OUTS")
                    print(f"TEAM {current_team.name} scored {current_game.score()} runs this inning")
                    print(f"--- END OF INNING ---\n")
                    current_team.score += current_game.score()
                    current_game.restart()
                    continue
            else:
                result = current_game.advance_bases(batter_hit)
                if result != 0:
                    print(f"TEAM {current_team.name} scored {result} runs this hit")

    print(f"FINAL RESULTS:")
    print(f"TEAM {player_1.name} SCORED {player_1.score} RUNS")
    print(f"TEAM {player_2.name} SCORED {player_2.score} RUNS")