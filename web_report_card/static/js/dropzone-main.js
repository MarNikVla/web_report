Dropzone.autoDiscover = false;
const myDropzone = new Dropzone('#my-dropzone', {
    url:'/upload/',
    autoProcessQueue: true,
    maxFiles: 1,
    maxFilesize: 3,
    // acceptedFiles:'.xlsx',
    addRemoveLinks: true,
    dictDefaultMessage: 'Загрузите табель рабочего времени',

})

$("#button").click(function (e) {
    top.location.href = 'result';
    e.preventDefault();

    myDropzone.processQueue();
});