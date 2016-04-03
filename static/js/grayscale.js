/*!
 * Start Bootstrap - Grayscale Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
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

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});
