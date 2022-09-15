Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'/upload/',
    maxFiles:5,
    maxFilesize:2,
    acceptedFiles:'.xlsx',
    addRemoveLinks: true,
    dictDefaultMessage: 'Upload your files here',
})
