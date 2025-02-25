from django.db import models

class TitleAkas(models.Model):
    titleId = models.CharField(max_length=255)
    ordering = models.IntegerField()
    title = models.CharField(max_length=255)
    region = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    types = models.JSONField()
    attributes = models.JSONField()
    isOriginalTitle = models.BooleanField()

    class Meta:
        unique_together = (("titleId", "ordering"),)
    
    def __str__(self):
        return f"{self.titleId} - {self.title}"
    

class TitleBasics(models.Model):
    tconst = models.CharField(max_length=255, primary_key=True)  # Clave primaria
    titleType = models.CharField(max_length=255)
    primaryTitle = models.CharField(max_length=255)
    originalTitle = models.CharField(max_length=255)
    isAdult = models.BooleanField()
    startYear = models.IntegerField(null=True, blank=True)
    endYear = models.IntegerField(null=True, blank=True)
    runtimeMinutes = models.IntegerField(null=True, blank=True)
    genres = models.JSONField(default=list)  # Array de strings

    def __str__(self):
        return self.primaryTitle
    

class TitleCrew(models.Model):
    tconst = models.OneToOneField(
        TitleBasics,
        on_delete=models.CASCADE,
        primary_key=True,  # Clave primaria
        related_name="crew"
    )
    directors = models.JSONField(default=list)  # Array de nconsts
    writers = models.JSONField(default=list)  # Array de nconsts

    def __str__(self):
        return f"Crew for {self.tconst}"
    


class TitleEpisode(models.Model):
    tconst = models.OneToOneField(
        TitleBasics,
        on_delete=models.CASCADE,
        primary_key=True,  # Clave primaria
        related_name="episode"
    )
    parentTconst = models.ForeignKey(
        TitleBasics,
        on_delete=models.CASCADE,
        related_name="episodes"
    )
    seasonNumber = models.IntegerField(null=True, blank=True)
    episodeNumber = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Episode {self.tconst} of {self.parentTconst}"
    

class TitlePrincipals(models.Model):
    tconst = models.ForeignKey(
        TitleBasics,
        on_delete=models.CASCADE,
        related_name="principals"
    )
    ordering = models.IntegerField()
    nconst = models.ForeignKey(
        "NameBasics",  # Referencia al modelo NameBasics
        on_delete=models.CASCADE,
        related_name="principals"
    )
    category = models.CharField(max_length=255)
    job = models.CharField(max_length=255, null=True, blank=True)
    characters = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = (("tconst", "ordering"),)  # Clave primaria compuesta

    def __str__(self):
        return f"{self.tconst} - {self.nconst} ({self.category})"
    


class TitleRatings(models.Model):
    tconst = models.OneToOneField(
        TitleBasics,
        on_delete=models.CASCADE,
        primary_key=True,  # Clave primaria
        related_name="rating"
    )
    averageRating = models.FloatField()
    numVotes = models.IntegerField()

    def __str__(self):
        return f"Rating for {self.tconst}: {self.averageRating}"
    

class NameBasics(models.Model):
    nconst = models.CharField(max_length=255, primary_key=True)  # Clave primaria
    primaryName = models.CharField(max_length=255)
    birthYear = models.IntegerField(null=True, blank=True)
    deathYear = models.IntegerField(null=True, blank=True)
    primaryProfession = models.JSONField(default=list)  # Array de strings
    knownForTitles = models.JSONField(default=list)  # Array de tconsts

    def __str__(self):
        return self.primaryName