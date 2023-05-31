$(document).ready(function () {
  function makeTranslat () {
    return $.get({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      dataType: 'json'
    });
  }
  makeTranslat().then((res) => {
    $('div#hello').text(res.hello);
  });
});