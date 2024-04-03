<!DOCTYPE html>
<html lang="en">
<head>
<title>Update Header Color</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<header class="red">This is the header</header>

<div id="red_header">Click me to make the header red</div>

<script>
 $(document).ready(function() {
        $('#red_header').click(function() {
            $('header').css('color', '#FF0000');
        });
    });
</script>

</body>
</html>
