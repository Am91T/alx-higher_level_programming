$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.ajax({
    url,
    dataType: 'json',
    success: function (data) {
      const movies = data.results;
      movies.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
