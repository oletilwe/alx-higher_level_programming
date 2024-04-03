<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Translate Hello</title>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<input type="text" id="language_code" placeholder="Enter language code (e.g., es, fr, en)">
<input type="button" id="btn_translate" value="Translate">
<div id="hello">Translation of "Hello" will appear here</div>

<script>
    $(document).ready(function() {
        $('#btn_translate').click(function() {
            var languageCode = $('#language_code').val();
            $.ajax({
                url: 'https://www.fourtonfish.com/hellosalut/hello/',
                dataType: 'json',
                data: { lang: languageCode },
                success: function(data) {
                    $('#hello').text(data.hello);
                },
                error: function() {
                    $('#hello').text('Translation not found');
                }
            });
        });
    });
</script>

</body>
</html>
