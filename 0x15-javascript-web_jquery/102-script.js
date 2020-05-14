$(document).ready( () => {
    $('INPUT#btn_translate').click( () => {
        let helloTranslate = $('INPUT#language_code').val();
        let url = 'https://fourtonfish.com/hellosalut/?lang=' + helloTranslate;
        $.get(url, function(data, textStatus) {
            console.log(url, data, textStatus);
            if (data.code !== 'none') {
                $('DIV#hello').text(data.hello);
            }
            else {
                $('DIV#hello').text('Invalid Language code');
            }
        });
    });
});