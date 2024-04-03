<!DOCTYPE html>
<html lang="en">
<head>
<title>Fetch Character Name</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<div id="character">Character Name Will Appear Here</div>

<script>
(document).ready(function() {
        $.ajax({
            url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
            dataType: 'json',
            success: function(data) {
                $('#character').text(data.name);
            },
            error: function() {
                $('#character').text('Failed to fetch character name');
            }
        });
    });
</script>

</body>
</html>
