<!DOCTYPE html>
<html lang="en">
<head>
<title>List Movies</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<ul id="list_movies"></ul>

<script>
$(document).ready(function() {
        $.ajax({
            url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
            dataType: 'json',
            success: function(data) {
                data.results.forEach(function(movie) {
                    $('#list_movies').append('<li>' + movie.title + '</li>');
                });
            },
            error: function() {
                $('#list_movies').append('<li>Failed to fetch movie titles</li>');
            }
        });
    });
</script>

</body>
</html>
