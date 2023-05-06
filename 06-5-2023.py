class Runner:
    def __init__(self, name, speed, run_time, rest_time):
        self.name = name
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time

    def distance_after(self, seconds):
        cycle_time = self.run_time + self.rest_time
        full_cycles = seconds // cycle_time
        remaining_time = seconds % cycle_time
        distance = full_cycles * self.run_time * self.speed
        if remaining_time > self.run_time:
            distance += self.run_time * self.speed
        else:
            distance += remaining_time * self.speed
        return distance

runners = [
    Runner('John', 10, 6, 20),
    Runner('James', 8, 8, 25),
    Runner('Jenna', 12, 5, 16),
    Runner('Josh', 7, 7, 23),
    Runner('Jacob', 9, 4, 32),
    Runner('Jerry', 5, 9, 18),
]

distances = [runner.distance_after(1234) for runner in runners]
winner_distance = max(distances)
winner_index = distances.index(winner_distance)
winner_name = runners[winner_index].name

print(f"The winner is {winner_name} with a distance of {winner_distance} meters.")

