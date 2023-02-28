import csv

import requests


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skil = main_skill
        self.main_skil_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_candidates(cls, path_to_file):
        if path_to_file.startswith('https'):
            res = requests.get(path_to_file)
            res.raise_for_status()
            source_file = res.text.splitlines()
        else:
            with open(path_to_file) as file:
                source_file = file.readlines()
        reader = csv.DictReader(source_file)
        cand_data_prepared = []
        for record in reader:
            candidate = dict(
                first_name=record['Full Name'].split(maxsplit=1)[0],
                last_name=record['Full Name'].split(maxsplit=1)[1],
                email=record['Email'],
                tech_stack=record['Technologies'].split('|'),
                main_skill=record['Main Skill'],
                main_skill_grade=record['Main Skill Grade']
            )
            cand_data_prepared.append(candidate)
        return [cls(**x) for x in cand_data_prepared]


if __name__ == '__main__':
    candidates = Candidate.generate_candidates('candidates.csv')
    candidates2 = Candidate.generate_candidates(
        'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
    print([x.full_name for x in candidates])
    print([x.full_name for x in candidates2])
