from django.db import models


# Create your models here.
class RatingsChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingsChoices.choices,
        default=RatingsChoices.G
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="users", null=True)
    movie_order = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="movies_users")

    def __str__(self) -> str:
        return f'<Movie {self.id} - {self.title}>'


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_user")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie")
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __repr__(self) -> str:
        return f"<MovieOrder {self.id} - {self.price}>"
    ...
