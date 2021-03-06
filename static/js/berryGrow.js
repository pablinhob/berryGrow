


var machines = {
  conf: null,
  status: null,

  render: function() {
    var that = this;





    var template_timer = _.template( $('#template_timer').html() );
    $('#timers_content').html('');

    var template_fan = _.template( $('#template_fan').html() );

    $('#control_content').html('');

    $.each( that.conf, function( i, machine ) {
      //console.log(machine.name, that.status[i].day.timer, that.status[i].night.timer);

      if( typeof that.status[i] != "undefined") {
        var stat = that.status[i];
      }
      else {
        var stat = false;
      }

      var machine_data = {
        id: i,
        machine: machine,
        status: stat
      };

      $('#timers_content').append( template_timer(machine_data) );
    });

    $.each( that.conf, function( i, machine ) {
      //console.log(machine.name, that.status[i].day.timer, that.status[i].night.timer);

      if( typeof that.status[i] != "undefined") {
        var stat = that.status[i];
      }
      else {
        var stat = false;
      }

      var machine_data = {
        id: i,
        machine: machine,
        status: stat
      };

      $('#control_content').append( template_fan(machine_data) );
    });



    $('input.timer_input').clockpicker({
        placement: 'bottom',
        autoclose: true
    });


    //$(".fan_power").ionRangeSlider();
    $(".fan_power").ionRangeSlider({
        min: 0,
        max: 100,


        postfix: " % "
    });

    $('input').change( function( ev ) {

      if ( $(ev.target).attr('data-is-numeric') == "true" ) {
        eval( 'that.' + $(ev.target).attr('data-machine-reference') + ' = ' + $(ev.target).val() + '  ;' )
      }
      else {
        eval( 'that.' + $(ev.target).attr('data-machine-reference') + ' = "' + $(ev.target).val() + '";' )
      }



      $.ajax({
        type: 'POST',
        url: '/setStatus',
        data: JSON.stringify( that.status ),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
      }).done(function(msg) {

      });
    })

  }
}




// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {

    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });
    // jQuery to collapse the navbar on scroll
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });



    // Ajax data calls
    $.when(
      $.ajax({'url':'/getStatus'}),
      $.ajax({'url': '/getConf' })
    ).done(function(statusJSON, confJSON){
      machines.conf = confJSON[0];
      machines.status = statusJSON[0];

      machines.render();
    });








/*
    // dark image
    Caman("#", function() {
        this.sunrise();
        this.render();
    });*/

  /*
  Caman("#intro-background", "/img/intro-bg.jpg", function () {
     this.sunrise();
     this.render();
   });*/
/*
   Caman("#canvas_img", "/img/intro-bg.jpg", function () {
     this.brightness(-30);
       this.render(function () {
        var img = this.toBase64();
        document.getElementById('intro-background').style.backgroundImage = "url(" + img + ")";
      });
   });

*/


});
