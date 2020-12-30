// using jQuery
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

$(document).ready(function() {
    $("#file_form").submit(function(event){
        event.preventDefault();
        console.log("abc")
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var filedata = new FormData(this);
        // filedata.append('fileSize',sizeConverter($('#file1')[0].files[0].size/1024));
        // filedata.append('file',$('#file1')[0].files[0]);
        // filedata.append('csrfmiddlewaretoken',csrftoken);
        $.ajax({
            url: "http://127.0.0.1:8000/analysis/save",
            headers:{
                "X-CSRFToken": csrftoken
            },
            type: "POST",
            async:true,
            cache: false,
            processData: false,
            contentType: false,
            enctype: "multipart/form-data",
            data: filedata,
            success: function(data){
                console.log("success");
                if(data.status =="Save"){
                    $('#graph').html(data.plt_div);

                }
            }
            
        })
    });

    


});


$(document).ready(function() {
    $("#btn2").click(function(event){
        event.preventDefault();
        var show = $(this).val();
        console.log(show);
        $.ajax({
            url: "http://127.0.0.1:8000/analysis/save",
            type: "GET",
            data: {
                'show':show
            },
            success: function(data){
                console.log("success");
                if(data.status =="Save"){
                    $('#graph').html(data.plt_div);
                }
            }
            
        })
    });
});

$(document).ready(function() {
    $("#btn1").click(function(event){
        event.preventDefault();
        var show = $(this).val();
        console.log(show);
        $.ajax({
            url: "http://127.0.0.1:8000/analysis/save",
            type: "GET",
            data: {
                'show':show
            },
            success: function(data){
                console.log("success");
                if(data.status =="Save"){
                    $('#graph').html(a+data.plt_div);
                }
            }
            
        })
    });
});