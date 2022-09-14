function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
$(document).ready(function () {
    $(".dropzone").dropzone({
        url: '/media/2/',

        headers: {
            'Accept': 'application/json',
            'Cooc': 'fdfdf',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        width: 300,
        height: 300,
        progressBarWidth: '100%',
        maxFileSize: '5MB',
    })
})
;