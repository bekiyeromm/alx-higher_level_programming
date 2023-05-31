$(document).ready(function() {
    $('#btn_translate').click(function() {
      var languageCode = $('#language_code').val();
      var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      });
    });
  });