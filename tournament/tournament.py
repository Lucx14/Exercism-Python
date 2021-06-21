from collections import OrderedDict
from typing import List, Set
import itertools


def short_format(text: str) -> str:
    return str(text).rjust(2, " ")


def long_format(text: str) -> str:
    return text.ljust(30, " ")


def flatten(l: list) -> list:
    return list(itertools.chain.from_iterable(l))


STAT_IDS = ["MP", "W", "D", "L", "P"]


class TableFormatter:
    DIV = " | "

    def __init__(self, data):
        self.data = data

    def call(self):
        return self.formatted_header() + self.formatted_body()

    def formatted_header(self) -> str:
        return [
            self.DIV.join(
                [long_format("Team")] + [short_format(col) for col in STAT_IDS]
            )
        ]

    def formatted_body(self) -> List[str]:
        return [
            self.DIV.join(
                [long_format(team)] + [short_format(stats[col]) for col in STAT_IDS]
            )
            for team, stats in self.data.items()
        ]


class Match:
    def __init__(self, result: str) -> None:
        self.teams, self.outcome = (result.split(";")[:2], result.split(";")[2])
        self.evaluate()

    def evaluate(self) -> None:
        if self.outcome == "draw":
            self.draw = True
        else:
            self.draw = False
            if self.outcome == "win":
                self.winner = self.teams[0]
                self.loser = self.teams[1]
            if self.outcome == "loss":
                self.winner = self.teams[1]
                self.loser = self.teams[0]


class TournamentTable:
    def __init__(self, results, match=Match, formatter=TableFormatter):
        self.matches = [match(result) for result in results]
        self.formatter = formatter
        self.tally_init()

    def tally_data(self):
        return {key: 0 for key in STAT_IDS}

    def tally_init(self) -> None:
        self.tally = {key: self.tally_data() for key in self.teams()}

    def teams(self) -> Set[str]:
        team_groups = [match.teams for match in self.matches]
        return set(flatten(team_groups))

    def calculate_scores(self) -> None:
        for match in self.matches:
            self.record_matches_played(match.teams)
            if match.draw:
                self.record_draw(match.teams)
            else:
                self.record_winner(match.winner)
                self.record_loser(match.loser)

    def record_matches_played(self, teams: List[str]) -> None:
        self.tally[teams[0]]["MP"] += 1
        self.tally[teams[1]]["MP"] += 1

    def record_winner(self, team: str) -> None:
        self.tally[team]["W"] += 1
        self.tally[team]["P"] += 3

    def record_loser(self, team: str) -> None:
        self.tally[team]["L"] += 1

    def record_draw(self, teams: List[str]) -> None:
        self.tally[teams[0]]["D"] += 1
        self.tally[teams[1]]["D"] += 1
        self.tally[teams[0]]["P"] += 1
        self.tally[teams[1]]["P"] += 1

    def sorted_tally(self):
        return OrderedDict(sorted(self.tally.items(), key=lambda i: (-i[1]["P"], i[0])))

    def produce_table(self):
        self.calculate_scores()
        return self.formatter(self.sorted_tally()).call()


def tally(rows):
    return TournamentTable(rows).produce_table()
