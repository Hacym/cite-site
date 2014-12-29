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
});