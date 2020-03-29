$('#detailed-form').on( "click", function( event ) {
    var data;
    $.ajax({
      url: "/music/api/",
      success: function( result ) {
       $( "#test" ).html( "Done" )
      $("#button-success").show()

      }
    }).then(() => {
        console.log('data after then:', data)
        }
    );
    $("#test" ).html( "Waiting..." )
    $("#button-success").hide()
});

