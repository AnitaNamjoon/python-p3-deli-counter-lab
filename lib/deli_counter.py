class DeliCounter:
    def __init__(self):
        self.queue = []

    def line(self):
        if not self.queue:
            return "The line is currently empty."
        else:
            return "The line is currently: " + " ".join(f"{i + 1}. {person}" for i, person in enumerate(self.queue))

    def take_a_number(self, name):
        self.queue.append(name)
        position = len(self.queue)
        return f"Welcome, {name}. You are number {position} in line."

    def now_serving(self):
        if not self.queue:
            return "There is nobody waiting to be served!"
        else:
            serving_person = self.queue.pop(0)
            return f"Currently serving {serving_person}."
