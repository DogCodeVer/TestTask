$(document).ready(function() {
    $('#id_address').suggestions({
      token: "f496e4b5f37cec8eb4c3dfa832cdfcf97088eaa6",
      type: "ADDRESS", //
      onSelect: function(suggestion) {
        console.log(suggestion);
        $('#id_address').val(suggestion.value);
    }
    });
  });