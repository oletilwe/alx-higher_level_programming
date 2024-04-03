<!DOCTYPE html>
<html lang="en">
<head>
<title>Update Header Text</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<header>This is the header</header>

<div id="update_header">Update Header</div>

<script>
$(document).ready(function() {
        $('#update_header').click(function() {
            $('header').text('New Header!!!');
        });
    });
</script>

</body>
</html>
