<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>List Operations</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<ul class="my_list"></ul>

<div id="add_item">Add Item</div>
<div id="remove_item">Remove Last Item</div>
<div id="clear_list">Clear List</div>

<script>
    $(document).ready(function() {
        $('#add_item').click(function() {
            $('.my_list').append('<li>Item</li>');
        });

        $('#remove_item').click(function() {
            $('.my_list li:last-child').remove();
        });

        $('#clear_list').click(function() {
            $('.my_list').empty();
        });
    });
</script>

</body>
</html>
