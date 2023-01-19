Dropzone.autoDiscover = false;
const myDropzone = new Dropzone('#my-dropzone', {
    url: '/upload/',
    autoProcessQueue: true,
    maxFiles: 1,
    maxFilesize: 3,
    // acceptedFiles:'.xlsx',
    addRemoveLinks: true,
    dictDefaultMessage: 'Upload your files here',

})

$("#button").click(function (e) {
    // redirect to url http://localhost/result/
    top.location.href = 'result';
    e.preventDefault();
    myDropzone.processQueue();
});