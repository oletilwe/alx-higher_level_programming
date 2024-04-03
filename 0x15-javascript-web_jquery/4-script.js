<!DOCTYPE html>
<html lang="en">
<head>
<title>Toggle Header Class</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<header class="red">This is the header</header>

<div id="toggle_header">Toggle Header Class</div>

<script>
$(document).ready(function() {
        $('#toggle_header').click(function() {
            $('header').toggleClass('red green');
        });
    });
</script>

</body>
</html>
