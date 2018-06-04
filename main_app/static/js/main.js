//$('button').on('click', function(event){
//    event.preventDefault();
//    var element = $(this);
//    $.ajax({
//        url : '/occupy/',
//        type : 'GET',
//        data : { gift_id : element.attr("data-id")},
//        success : function(response){
//            element.html(' ' + response);
//        }
//    });
//});

$('#form').submit(function(e){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : '/occupy/',
        type : 'GET',
        data : { gift_id : element.attr("data-id")},
        success : function(response){
            element.html(' ' + response);
        }
    });
});