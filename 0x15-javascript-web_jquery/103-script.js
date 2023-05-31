$(document).ready(function() {
    function fetchTranslation() {
      const languageCode = $('#language_code').val();
      const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      });
    }
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Enter key pressed
        fetchTranslation();
      }
    });
  });