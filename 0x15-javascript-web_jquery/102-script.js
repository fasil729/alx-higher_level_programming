$(document).ready(function() {
    $("#btn_translate").click(function() {
      const languageCode = $("#language_code").val();
      if (languageCode !== "") {
        const url = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;
        $.get(url, function(data) {
          $("#hello").text(data.hello);
        });
      }
    });
  });