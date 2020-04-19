class Competitor:


    def __init__(self, name, position, height, gender, startTimestamp, intervalMs=10):
        self.name = name
        self.position = position
        self.height = height
        self.gender = gender
        self.lastReading = startTimestamp
        self.numberOfSquats = 0
        self.squatsPerInterval = 0

    def get_total_number_of_squats(self):
        """Good enough for first visualisation with barcharts or numbers just next to eachother"""
        return self.numberOfSquats

    def add_squats(self, squats, readingTimestamp):
        self.numberOfSquats += squats
        timepassed = readingTimestamp - self.lastReading
        self.squatsPerInterval = squats / timepassed

    def get_squats_per_interval(self):
        return self.squatsPerInterval







