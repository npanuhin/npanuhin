from collections import defaultdict
import os

import jstyleson as json

UnsolvableProblemsType = dict[str, list[str]]


class UnsolvableProblems:
    def __init__(self, path: str):
        self.path = path
        if not os.path.exists(self.path) or os.stat(self.path).st_size == 0:
            self._write({})

        self.cached_data = None

    def _read(self) -> UnsolvableProblemsType:
        if self.cached_data is None:
            with open(self.path, 'r', encoding="utf-8") as file:
                self.cached_data = defaultdict(list, json.load(file))
        return self.cached_data

    def _write(self, data: UnsolvableProblemsType):
        self.cached_data = sorted(data)
        with open(self.path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def check(self, contest_id: int, problem_name: str) -> bool:
        unsolvable = self._read()
        return problem_name in unsolvable.get(str(contest_id), {})

    def add(self, contest_id: int, problem_name: str):
        contest_id = str(contest_id)

        unsolvable = self._read()
        unsolvable[contest_id].append(problem_name)
        self._write(unsolvable)


# For testing purposes
if __name__ == "__main__":
    if os.path.exists("test.json"):
        os.remove("test.json")

    unsolvable_problems = UnsolvableProblems("test.json")
    unsolvable_problems.add(1, "A")
    unsolvable_problems.add(1, "B")
    unsolvable_problems.add(2, "C")
