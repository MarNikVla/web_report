Dropzone.autoDiscover = false;
const myDropzone = new Dropzone('#my-dropzone', {
    // url:'/upload/',
    autoProcessQueue: true,
    maxFiles: 5,
    maxFilesize: 2,
    // acceptedFiles:'.xlsx',
    addRemoveLinks: true,
    dictDefaultMessage: 'Upload your files here',

})

// $("#button").click(function (e) {
//     e.preventDefault();
//     myDropzone.processQueue();
// });