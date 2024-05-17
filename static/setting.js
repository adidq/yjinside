// /setting에서 변경가능하게 할예정
// spa, darkmode
function setDark() {

}

function setSpa() {
    //spa 토글기능
} //다크모드 토클기능
    //data-theme="dark"
    //data-theme="light

$(document).ready(function() {
    $('#toggleTheme').click(function() {
        var $themeElement = $('html');
        var currentTheme = $themeElement.attr('data-theme');

        if (currentTheme === 'light') {
            $themeElement.attr('data-theme', 'dark');
            $('#toggleTheme').text('라이트 테마로');
        } else {
            $themeElement.attr('data-theme', 'light');
            $('#toggleTheme').text('다크 테마로');
        }
    });
});