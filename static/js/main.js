$(function(){
    $("#nav li").click(function(){
        var dropdown = $(this).find('ul');
        if ($('#nav li').hasClass('active')){
            if($('#nav li.active')[0] == this) return $(this).removeClass('active');
            $('#nav li').removeClass('active');
        }

        $(this).addClass('active');

    })
});