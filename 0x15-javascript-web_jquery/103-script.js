$(document).ready(function () {
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.ajax({
      url,
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});
