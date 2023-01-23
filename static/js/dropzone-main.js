Dropzone.autoDiscover = false;
const myDropzoneTable = new Dropzone('#my-dropzone', {
    url:'/upload/',
    autoProcessQueue: true,
    maxFiles: 1,
    maxFilesize: 3,
    // acceptedFiles:'.xlsx',
    addRemoveLinks: true,
    dictDefaultMessage: 'Загрузите файл .xlsx',

})


$("#table_button").click(function (e) {
    top.location.href = 'table-result';
    e.preventDefault();

    myDropzoneTable.processQueue();
});

$("#grafik_button").click(function (e) {
    top.location.href = 'grafik-result';
    e.preventDefault();

    myDropzoneGrafik.processQueue();
});