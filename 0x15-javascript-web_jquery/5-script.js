<!DOCTYPE html>
<html lang="en">
<head>
<title>Add Item to List</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<ul class="my_list">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

<div id="add_item">Add Item</div>

<script>
$(document).ready(function() {
        $('#add_item').click(function() {
            $('.my_list').append('<li>Item</li>');
        });
    });
</script>

</body>
</html>
