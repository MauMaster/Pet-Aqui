$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,

    start: function (e) {
      $("#modal-progress").modal("show");
      
      
    },

    stop: function (e) {
    $("#modal-progress").modal("hide");
    $('#modal-progress2').modal('show');
setTimeout(function () {
    $('#modal-progress2').modal('hide')
}, 3000);
    
window.setTimeout(function (e) {
  location.href = "http://127.0.0.1:8000/progress-bar-upload";
}, 2000);
      
    },
    
    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },

    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
          
        )
        
      }
      
    }

  });

});