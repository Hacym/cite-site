$(document).ready(function(){
    $(".quotemarks").change(function() {
        if ($(this).val() == "False") {
            $(".logo").show();
        } else {
            $(".logo").hide();
        }
    });
    
    $(".logo").change(function() {
        if ($(this).val() == "True") {
            $(".imagefile").show();
        } else {
            $(".imagefile").hide();
        }
    });
    
    $("form").on('input change', ':input', function(event) {
        $.ajax({
            type: "POST",
            url: "create_image",
            data: $("#form").serialize(),
            success: function(msg){
                $("#error").hide();
                $("#image").show();
                $("#previewimage").attr("src", msg);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {                
                $("#image").hide();
                $("#error").show();
                $("#error").html(XMLHttpRequest.responseText);
            }
        });
    });
});