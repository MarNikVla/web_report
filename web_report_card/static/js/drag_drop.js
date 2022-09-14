$("document").ready(function() {
  $(".child").draggable({
    revert: true
  });

  $(".parent").droppable({
    accept: '.child',
    drop: function(event, ui) {
      $(this).append($(ui.draggable));
    }
  });
});