


var machines = {
  conf: null,
  status: null,

  render: function() {
    var that = this;





    var template_timer = _.template( $('#template_timer').html() );
    $('#timers_content').html('');


    $.each( that.conf, function( i, machine ) {
      console.log(machine.name, that.status[i].day.timer, that.status[i].night.timer);

      var machine_data = {
        id: i,
        machine: machine,
        status: that.status[i]
      };

      $('#timers_content').append( template_timer(machine_data) );
    });


    var input = $('.timer_input').clockpicker({
        placement: 'bottom',

        autoclose: true
    });
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
   });*/




});
