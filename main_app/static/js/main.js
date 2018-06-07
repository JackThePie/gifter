$('button').on('click', function(event){
    event.preventDefault();
    var formData = $('form').serializeArray();
//    var formData = 'test';
    var element = $(this);
    $.ajax({
        url : '/occupy/',
        type : 'GET',
        data : { gift_id : element.attr("data-id"),
                 form_data : formData},
        success : function(response){
//            element.html(' ' + response);
            location.reload();
        }
    });
});

//$('#form').submit(function(event){
//    event.preventDefault();
//    var formData = $(this).serialize();
//    var element = $(this);
//    $.ajax({
//        url : '/occupy/',
//        type : 'GET',
////        data : formData,
//        data : { gift_id : element.attr("data-id")},
//        success : function(response){
//            element.html(' ' + response);
//        }
//    });
//});