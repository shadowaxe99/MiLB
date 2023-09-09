class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    batting_average = models.FloatField()
    home_runs = models.IntegerField()
    runs_batted_in = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    division = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"