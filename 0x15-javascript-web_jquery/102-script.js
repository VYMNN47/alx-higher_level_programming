$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const l = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${l}`;
    $.get(url, function (response) {
      $('div#hello').text(response.hello);
    });
  });
});
