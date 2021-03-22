 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

 $(document).ready(function() {
    //  for jquery data tables
    $('#myTable').DataTable();

    $('#add-product-form').on('submit', function(e) {
        e.preventDefault();
        var data = new FormData($('form').get(0));
       //Create AJAX Call
       $.ajax({
           type: "POST",
           url: "/new-product/",
           data: data,
           cache: false,
           processData: false,
           contentType: false,
           beforeSend: function(xhr, settings) {
                        var csrftoken = getCookie('csrftoken');
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
           success: function(response){
                //reset the form after successful submit
                $("#add-product-form")[0].reset();
                $("#myModal").modal('show');
//                $(this)[0].reset();
           },
           error : function(response){
                console.log('Error aai gyi..........!!!!!!!!!!!-----------------')
                console.log(response);
           }
       });
    });
});
