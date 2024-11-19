from collections import defaultdict
import os

import jstyleson as json


InvalidSubmissionsType = dict[str, dict[str, list[int]]]


class InvalidSubmissions:
    def __init__(self, path: str):
        self.path = path
        if not os.path.exists(self.path) or os.stat(self.path).st_size == 0:
            self._write({})

    def _read(self) -> InvalidSubmissionsType:
        with open(self.path, 'r', encoding="utf-8") as file:
            invalid_submissions = defaultdict(dict, json.load(file))

        for contest_id in invalid_submissions:
            invalid_submissions[contest_id] = defaultdict(list, invalid_submissions[contest_id])

        return invalid_submissions

    def _write(self, data: InvalidSubmissionsType):
        with open(self.path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def check(self, contest_id: int, problem_name: str, submission_id: int) -> bool:
        invalid_submissions = self._read()
        return submission_id in invalid_submissions.get(str(contest_id), {}).get(problem_name, [])

    def add(self, contest_id: int, problem_name: str, submission_id: int):
        contest_id = str(contest_id)

        invalid_submissions = self._read()

        # Have to do this because defaultdict doesn't call __setitem__ on nested dicts
        if contest_id not in invalid_submissions:
            invalid_submissions[contest_id] = defaultdict(list)

        invalid_submissions[contest_id][problem_name].append(submission_id)
        self._write(invalid_submissions)


# For testing purposes
if __name__ == "__main__":
    if os.path.exists("test.json"):
        os.remove("test.json")

    invalid_submissions = InvalidSubmissions("test.json")
    invalid_submissions.add(1, "A", 1)
    invalid_submissions.add(1, "B", 2)
    invalid_submissions.add(2, "C", 3)
