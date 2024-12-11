$(document).ready(function() {
    // Проверяем, что элемент с id='id_address' существует
    if ($('#id_address').length) {
        $('#id_address').suggestions({
            token: "f496e4b5f37cec8eb4c3dfa832cdfcf97088eaa6",  // Ваш API ключ DaData
            type: "ADDRESS",
            count: 5,  // Количество предложений для автозаполнения
            /* дополнительные настройки */
        });
    }
});
