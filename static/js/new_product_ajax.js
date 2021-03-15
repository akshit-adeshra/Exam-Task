 $(document).ready(function() {
     $("#product-success-msg").hide();

     var myform = $('#add-product-form');
     myform.submit(function(e){
                 $("#product-success-msg").show();

    });
});                 

//         e.preventDefault();
//         var formData = $(this).serialize();
//         $.ajax({
//             method: "POST",
//             url: myform.attr("data-url"),
//             data: formData,
//             success: handleFormSuccess,
//             error: handleFormError,
//         });

//         function handleFormSuccess(data, textStatus, jqXHR) {
//             console.log(data);
//             if (data['status'] == 'Save') {
//                 $("#product-success-msg").show();
//             }
//             // console.log(textStatus);
//             // console.log(jqXHR);
//             myform[0].reset();
//         }

//         function handleFormError(jqXHR, textStatus, errorThrown) {
//             console.log(jqXHR);
//             console.log(textStatus);
//             console.log(errorThrown);
//         }
