class MonkeyBananaProblem:
    def __init__(self):
        self.states = {"monkey": "floor", "banana": "ceiling", "chair": "corner", "monkey_on_chair": False, "banana_reached": False}

    def move_monkey(self, location):
        self.states["monkey"] = location
        print(f"Monkey moves to the {location}")

    def move_chair(self, location):
        self.states["chair"] = location
        print(f"Chair moves to the {location}")

    def climb_chair(self):
        if self.states["monkey"] == self.states["chair"]:
            self.states["monkey_on_chair"] = True
            print("Monkey climbs onto the chair")

    def grab_banana(self):
        if self.states["monkey_on_chair"]:
            self.states["banana_reached"] = True
            print("Monkey grabs the banana")

    def solve_problem(self):
        self.move_monkey("corner")
        self.move_chair("under the banana")
        self.move_monkey("under the banana")
        self.climb_chair()
        self.grab_banana()

if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    problem.solve_problem()