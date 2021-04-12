import itertools


class Allergies:
    allergens = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score):
        self.score = score % self.cutoff()
        self.combinations = self.generate_combinations()

    def cutoff(self):
        return sum(allergen[1] for allergen in self.allergens) + 1

    def generate_combinations(self):
        return (
            combination
            for number_of_allergens in range(1, len(self.allergens) + 1)
            for combination in itertools.combinations(
                self.allergens, number_of_allergens
            )
        )

    def allergic_to(self, item):
        return item in self.lst

    def score_match(self, combination):
        return sum(item[1] for item in combination) == self.score

    @property
    def lst(self):
        if self.score is 0:
            return []

        allergen_list = next(filter(self.score_match, self.combinations))
        return [item[0] for item in allergen_list]



# class Allergies:
#     ALLERGIES = {
#         "eggs": 1,
#         "peanuts": 2,
#         "shellfish": 4,
#         "strawberries": 8,
#         "tomatoes": 16,
#         "chocolate": 32,
#         "pollen": 64,
#         "cats": 128,
#     }
#
#     def __init__(self, score):
#         self.score = score
#
#     def allergic_to(self, item):
#         return bool(self.score & Allergies.ALLERGIES[item])
#
#     @property
#     def lst(self):
#         return [allergy for allergy in Allergies.ALLERGIES if self.allergic_to(allergy)]
