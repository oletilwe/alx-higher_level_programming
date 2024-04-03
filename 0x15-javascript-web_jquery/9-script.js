<!DOCTYPE html>
<html lang="en">
<head>
<title>Fetch and Display Translation of Hello</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<div id="hello">Translation of "hello" will appear here</div>

<script>
$(document).ready(function() {
        $.ajax({
            url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
            dataType: 'json',
            success: function(data) {
                $('#hello').text(data.hello);
            },
            error: function() {
                $('#hello').text('Failed to fetch translation');
            }
        });
    });
</script>

</body>
</html>
