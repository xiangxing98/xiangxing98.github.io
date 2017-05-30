$(document).ready(function(){
    $('#book-chapters-trigger').click(function(){
        $(this).toggleClass('active');
        $('#chapters-dropdown').toggle();
    });
    $(document).click(function(event){
        $target = $(event.srcElement || event.target)
        if(!$target.is('#book-chapters-trigger') && !$target.is('#chapters-dropdown,#chapters-dropdown *')) {
            $('#chapters-dropdown').hide();
            $('#book-chapters-trigger').removeClass('active');
        }
    });

    prettyPrint();
});