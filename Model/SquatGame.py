class SquatGame:
    def __init__(self, competitors, startingTime):
        self.competitors = competitors
        self.startingTime = startingTime

    def get_competitors(self):
        return self.competitors

    def get_current_squats_per_interval(self):
        """return json object with current squats per interval for all competitors; useful for where momentum needs to be plotted"""
        x  = {}
        for competitor in self.competitors:
            x[competitor.name] =  competitor.squatsPerInterval
        return x

    def get_total_squats(self):
        """returns the total number of squats for all competitors as JSON object; useful if only ranking needed"""
        x  = {}
        for competitor in self.competitors:
            x[competitor.name] =  competitor.get_total_number_of_squats()
        return x