class Edge:
    def __init__(self, start, end, weight=0):
        self.start = start
        self.end = end
        self.weight = weight

    def __hash__(self):
        return hash((self.start, self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return f"start: {self.start}, end: {self.end}, weight: {self.weight}"
