function hover(element) {
	setTimeout(function() {
		element.setAttribute('src', '/static/assets/img/order-red.svg');
	}, 150)
}

function unhover(element) {
	setTimeout(function() {
		element.setAttribute('src', '/static/assets/img/order.svg');
	}, 150)
}

function unhoverBlack(element) {
	setTimeout(function() {
		element.setAttribute('src', '/static/assets/img/order-black.svg');
	}, 150)
}

    //show baidu map
    var long, lat;
    function getLocation()
    {
        if (navigator.geolocation)
        {
            navigator.geolocation.getCurrentPosition(showPosition);
        }
    }
    
    function showPosition(position)
    {
		long = localStorage.getItem("long");
		lat = localStorage.getItem("lat");
		if(!long){
			long = position.coords.longitude; 
			lat = position.coords.latitude;
			localStorage.setItem("long", long);
			localStorage.setItem("lat", lat);
		}
        
		baidu(long, lat);
    }
    function baidu(long, lat){
		var map = new BMap.Map("container"); 
        var point = new BMap.Point(long,lat); 
        map.centerAndZoom(point, 15);  
        map.enableScrollWheelZoom(true);    
        map.addControl(new BMap.NavigationControl());    
        map.addControl(new BMap.ScaleControl());    
        map.addControl(new BMap.OverviewMapControl());    
		map.addControl(new BMap.MapTypeControl());    
		var marker = new BMap.Marker(point);
		map.addOverlay(marker);
    }
    $(document).ready(function () {
		var path = window.location.href.toString();
		if(path.endsWith("/my-account.html")){
			getLocation();
			//! deployment version
			// long = 103.995;
			// lat = 30.794;
			// baidu(long, lat);
		}
        
	});



jQuery(function ($) {
    'use strict';

        // Header Sticky
		$(window).on('scroll',function() {
            if ($(this).scrollTop() > 120){  
                $('.navbar-area').addClass("is-sticky");
            }
            else{
                $('.navbar-area').removeClass("is-sticky");
            }
		});

		// Mean Menu
		jQuery('.mean-menu').meanmenu({
			meanScreenWidth: "991"
        });
		
		// Others Option For Responsive JS
		$(".others-option-for-responsive .dot-menu").on("click", function(){
			$(".others-option-for-responsive .container .container").toggleClass("active");
        });
        
        // Button Hover JS
		$('.default-btn')
		.on('mouseenter', function(e) {
			var parentOffset = $(this).offset(),
			relX = e.pageX - parentOffset.left,
			relY = e.pageY - parentOffset.top;
			$(this).find('span').css({top:relY, left:relX})
		})
		.on('mouseout', function(e) {
			var parentOffset = $(this).offset(),
			relX = e.pageX - parentOffset.left,
			relY = e.pageY - parentOffset.top;
			$(this).find('span').css({top:relY, left:relX})
		});

		// Nice Select JS
		$('select').niceSelect();

		// Newsletter Modal JS
		var path = window.location.href.toString();
		if(path.endsWith("/")||path.endsWith("/index.html")||path.endsWith("/index-2.html")||path.endsWith("/index-3.html")
		||path.endsWith("/index-4.html")){
			if(pop=="1"){
			$('#newsletter-modal').modal({
				show: true
			});
			}
			else{
				$('#newsletter-modal').modal({
					show: false
				});
			}
		}

		// Home Slides
		$('.home-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: false,
            autoplayHoverPause: true,
            items: 1,
            smartSpeed: 1000,
			autoplay: false,
            navText: [
                "<i class='flaticon-left-arrow'></i>",
                "<i class='flaticon-right-arrow'></i>"
            ],
		});
        $(".home-slides").on("translate.owl.carousel", function(){
            $(".main-slider-content b").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content h1").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content a").removeClass("animated fadeInUp").css("opacity", "0");
		});
        $(".home-slides").on("translated.owl.carousel", function(){
            $(".main-slider-content b").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content h1").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content a").addClass("animated fadeInUp").css("opacity", "1");
		});
		
		// Home Slides Two
		$('.home-slides-two').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
            autoplayHoverPause: true,
            items: 1,
            smartSpeed: 100,
			autoplay: false,
		});
		$(".home-slides-two").on("translate.owl.carousel", function(){
            $(".main-slider-content b").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content h1").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-slider-content a").removeClass("animated fadeInUp").css("opacity", "0");
		});
        $(".home-slides-two").on("translated.owl.carousel", function(){
            $(".main-slider-content b").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content h1").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-slider-content a").addClass("animated fadeInUp").css("opacity", "1");
		});
		
        // Partner Slider
		$('.partner-slider').owlCarousel({
			loop: true,
			nav: false,
			dots: false,
			smartSpeed: 500,
			margin: 30,
			autoplayHoverPause: true,
            autoplay: true,
			responsive: {
				0: {
					items: 2
				},
				576: {
					items: 2
				},
				768: {
					items: 3
				},
				1024: {
					items: 4
				},
				1200: {
					items: 5
				}
			}
		});

		// Products Details Image Slides
		$('.products-details-image-slides').slick({
			dots: true,
			speed: 500,
			fade: false,
			slide: 'li',
			slidesToShow: 1,
			autoplay: true,
			autoplaySpeed: 4000,
			prevArrow: false,
    		nextArrow: false,
			responsive: [{
				breakpoint: 800,
				settings: {
					arrows: false,
					centerMode: false,
					centerPadding: '40px',
					variableWidth: false,
					slidesToShow: 1,
					dots: true
				},
				breakpoint: 1200,
				settings: {
					arrows: false,
					centerMode: false,
					centerPadding: '40px',
					variableWidth: false,
					slidesToShow: 1,
					dots: true
				}
			}],
			customPaging: function (slider, i) {
				return '<button class="tab">' + $('.slick-thumbs li:nth-child(' + (i + 1) + ')').html() + '</button>';
			}
		});
		
		// Testimonial Slides
		$('.testimonial-slides').owlCarousel({
			loop: true,
			nav: true,
			dots: false,
            autoplayHoverPause: true,
            items: 1,
            smartSpeed: 100,
			autoplay: false,
            navText: [
                "<i class='flaticon-left-arrow'></i>",
                "<i class='flaticon-right-arrow'></i>"
            ],
		});

		// Main Products Image Slides
		$('.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			asNavFor: '.slider-nav'
		});
		$('.slider-nav').slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			asNavFor: '.slider-for',
			dots: false,
			arrows: false,
			focusOnSelect: true,
			verticalSwiping: true,
			vertical: true
		});
		$('a[data-slide]').on('click', function(e) {
			e.preventDefault();
			var slideno = $(this).data('slide');
			$('.slider-nav').slick('slickGoTo', slideno - 1);
		});
		
		// Tabs
		$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
		$('.tab ul.tabs li a').on('click', function (g) {
			var tab = $(this).closest('.tab'), 
			index = $(this).closest('li').index();
			tab.find('ul.tabs > li').removeClass('current');
			$(this).closest('li').addClass('current');
			tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
			tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
			g.preventDefault();
		});

		// Count Time 
		function makeTimer() {
			var endTime = new Date("December 7, 2020 20:39:00 PDT");			
			var endTime = (Date.parse(endTime)) / 1000;
			var now = new Date();
			var now = (Date.parse(now) / 1000);
			var timeLeft = now - endTime;
			var days = Math.floor(timeLeft / 86400); 
			var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
			var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
			var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
			if (hours < "10") { hours = "0" + hours; }
			if (minutes < "10") { minutes = "0" + minutes; }
			if (seconds < "10") { seconds = "0" + seconds; }
			$("#days").html(days + "<span>Days</span>");
			$("#hours").html(hours + "<span>Hours</span>");
			$("#minutes").html(minutes + "<span>Minutes</span>");
			$("#seconds").html(seconds + "<span>Seconds</span>");
		}
		setInterval(function() { makeTimer(); }, 0);

		// Products Filter Options
        $(".icon-view-two").on("click", function(e){
			e.preventDefault();
			document.getElementById("products-collections-filter").classList.add('products-col-two')
			document.getElementById("products-collections-filter").classList.remove('products-col-one', 'products-col-three', 'products-col-four', 'products-row-view');
		});
		$(".icon-view-three").on("click", function(e){
			e.preventDefault();
			document.getElementById("products-collections-filter").classList.add('products-col-three')
			document.getElementById("products-collections-filter").classList.remove('products-col-one', 'products-col-two', 'products-col-four', 'products-row-view');
		});
        $('.products-filter-options .view-column a').on('click', function(){
            $('.view-column a').removeClass("active");
            $(this).addClass("active");
		});
		
		// Range Slider
        $( "#range-slider" ).slider({
			range: true,
			min: 50,
			max: 400,
			values: [50, 400],
			slide: function( event, ui ) {
				$( "#price-amount" ).val( "$" + ui.values[ 0 ] + "-$" + ui.values[ 1 ] );
			}
		});
		$( "#price-amount" ).val( "$" + $( "#range-slider" ).slider( "values", 0 ) +
		" - $" + $( "#range-slider" ).slider( "values", 1 ) );  

		// Popup Video
		$('.popup-youtube').magnificPopup({
			disableOn: 320,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
		});

		// FAQ Accordion
		$('.accordion').find('.accordion-title').on('click', function(){
			$(this).toggleClass('active');
			$(this).next().slideToggle('fast')
			$('.accordion-content').not($(this).next()).slideUp('fast');
			$('.accordion-title').not($(this)).removeClass('active');		
		});

		// Odometer JS
        $('.odometer').appear(function(e) {
			var odo = $(".odometer");
			odo.each(function() {
				var countNumber = $(this).attr("data-count");
				$(this).html(countNumber);
			});
		});
		

		/* Sign Up Form */
		$("#signUpForm").validator().on("submit", function(event) {
			if (event.isDefaultPrevented()) {
				formErrorS();
				$(".warning")[0].innerText = "Some fields are blank or wrong form of email address!";
			} else {
				if($('#password').val().length<8){
					formErrorS();
					$(".warning")[0].innerText = "Password length should over 8 characters";
					event.preventDefault();
				}
				else{
					event.preventDefault();
					ssubmitForm();
				}

				
			}
		});
	
		function ssubmitForm() {
			var email = $("#email").val();
			var name = $("#name").val();
			var password = $("#password").val();
			var question = $("#question").val();
			var answer = $("#answer").val();
			var path = window.location.href.toString();
			$.post(path,{username: name, password: password, email:email, question:question, answer:answer},
				function(data){
					if(data == '1'){
						var href = "./index.html";
						window.location.replace(href);
					}
					else{
						formErrorS();
						$(".warning")[0].innerText = data;
					}
				}); 
		}

		$("#modal-form").validator().on("submit", function(event) {
			if (event.isDefaultPrevented()) {
				formErrorM();
				
			} else {
				event.preventDefault();
				submitFormModal();
			}
		});
	
		function submitFormModal() {
			var email = $("#email").val();
			var password = $("#password").val();
			var remember = $("#remember-me").is(':checked');;
			var path = window.location.href.toString();
			var last = path.lastIndexOf("/");
			var newPath = path.substring(0,last) + "/login.html"
        $.post(newPath,{email: email, password: password,remember: remember},
            function(data){
                if(data == '1'){
                    var href = "./index.html";
                    window.location.replace(href);
                }
                else{
					formErrorM();
                    $(".warning")[0].innerText = data;
                }
            }); 
		}

		/* Log in Form */
		$("#loginForm").validator().on("submit", function(event) {
			if (event.isDefaultPrevented()) {
				formErrorL();
			} else {
				event.preventDefault();
				lsubmitForm();
			}
		});
	
		function lsubmitForm() {
			var email = $("#email").val();
			var password = $("#password").val();
			var remember = $("#remember-me").is(':checked');;
			var path = window.location.href.toString();
        $.post(path,{email: email, password: password,remember: remember},
            function(data){
                if(data == '1'){
                    var href = "./index.html";
                    window.location.replace(href);
                }
                else{
                    formErrorL();
					$(".warning")[0].innerText = data;
                }
            });  
		}


		$("#forgetForm").validator().on("submit", function(event) {
			if (event.isDefaultPrevented()) {
				formErrorForget();
			} else {
				var password = $("#password").val();
				if(password.length<8){
					event.preventDefault();
					$(".warning")[0].innerText = "password length should over 8 characters.";
					$("#forgetForm").addClass("animated shake");
					setTimeout(function() {
						$("#forgetForm").removeClass("animated shake");
					}, 1000)
				}
				else{
					event.preventDefault();
					submitFormForget();
				}
				
			}
		});
	
		function submitFormForget() {
			var email = $("#email").val();
			var password = $("#password").val();
			var question = $("#question").val();
			var answer = $("#answer").val();
			var path = window.location.href.toString();
        $.post(path,{email: email, password: password, answer:answer, question:question},
            function(data){
                if(data == '1'){
                    var href = "./login.html";
                    window.location.replace(href);
                }
                else{
                    formErrorForget();
                    setTimeout(function() {
						$(".warning")[0].innerText = data;
						$("#forgetForm").addClass("animated shake");
						setTimeout(function() {
							$("#forgetForm").removeClass("animated shake");
						}, 1000)
					}, 500)
                }
            });  
		}
		
		function formErrorS(){
			$("#signUpForm").addClass("animated shake");
			setTimeout(function() {
				$("#signUpForm").removeClass("animated shake");
			}, 1000)
		}

		function formErrorM(){
			$("#modal-form").addClass("animated shake");
			setTimeout(function() {
				$("#modal-form").removeClass("animated shake");
			}, 1000)
		}

		function formErrorL(){
			$("#loginForm").addClass("animated shake");
			setTimeout(function() {
				$("#loginForm").removeClass("animated shake");
			}, 1000)
		}

		function formErrorForget(){
			$("#forgetForm").addClass("animated shake");
			setTimeout(function() {
				$("#forgetForm").removeClass("animated shake");
			}, 1000)
		}

		function submitMSGSub(valid, msg){
			if(valid){
				var msgClasses = "validation-success";
			} 
			else {
				var msgClasses = "validation-danger";
			}
			$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
		}


		function convertId(name){
			var names = {"Bluetooth Headphone":1,"Protable Speakers":2,"Digital Camera":3,"Smart Watch":4,"New Smart Phone":5}
			return names[name]
		}

		function convertName(id){
			var ids = {1:"Bluetooth Headphone",2:"Protable Speakers",3:"Digital Camera",4:"Smart Watch",5:"New Smart Phone"}
			return ids[id]
		}

		$('#update').click(function(){
			var cart_data={
				'products': [
				],
			};

			var table = $('.table.table-bordered tbody')[0];
			var product_sum = 0;
			var count = 0;
			var amount = 0;
			for(var i=0;i<table.children.length;i++){
				amount = parseInt(table.children[i].children[3].children[0].children[1].value);
				if(amount>0){
					cart_data.products[count] = {"id": convertId(table.children[i].children[1].innerText),
					"name": table.children[i].children[1].innerText,
					"price":parseFloat(table.children[i].children[2].innerText.substr(1)),
					"quantity": amount,
						"sum":parseFloat(table.children[i].children[4].innerText.substr(1))}
						product_sum += amount;	
						count++;
				}
				amount=0;
			}
			cart_data.total = parseFloat($('.cart-totals ul li span')[2].innerText.substr(1)) - 30;
			cart_data.product_sum = product_sum;

			var data= {
				data: JSON.stringify(cart_data),
			}
			var last = path.lastIndexOf("/");
			var new_path = path.substring(0,last) + "/updateCart"
			$.ajax({
				type: "POST",
				data :data,
				url: new_path,
				dataType: 'json',
				success:function(res){
						var href = "./cart.html";
						window.location.replace(href);
				}
			});
		});

		$('#checkout').click(function(){
			var cart_data={
							'products': [
							],
						};

			var table = $('.table.table-bordered tbody')[0];
			var product_sum = 0;
			var amount = 0;
			var count = 0;
			for(var i=0;i<table.children.length;i++){
				amount = parseInt(table.children[i].children[3].children[0].children[1].value);
				if(amount>0){
					cart_data.products[count] = {"id": convertId(table.children[i].children[1].innerText),
					"name": table.children[i].children[1].innerText,
					"price":parseFloat(table.children[i].children[2].innerText.substr(1)),
					"quantity": amount,
						"sum":parseFloat(table.children[i].children[4].innerText.substr(1))}
						product_sum += amount;	
						count++;
				}
				amount=0;
			}
			cart_data.total = parseFloat($('.cart-totals ul li span')[2].innerText.substr(1));
			cart_data.product_sum = product_sum;

			var data= {
				data: JSON.stringify(cart_data),
			}
	
			$.ajax({
				type: "POST",
				data :data,
				url: path,
				dataType: 'json',
				success:function(res){
                    if(res=="1"){
						var href = "./order-success.html";
						window.location.replace(href);
					}
				}
			});
		});


		$(".cart-totals").each(function () { 
			var table = $('.table.table-bordered tbody')[0];
			var sum = 0;
			for(var i=0;i<table.children.length;i++){
				sum += parseFloat(table.children[i].children[4].innerText.substr(1));
			}
			$('.cart-totals li:first-child span')[0].innerText ="$" + sum.toFixed(2);

			var subtotal = parseFloat($('.cart-totals ul li span')[0].innerText.substr(1));
			var shipping = parseFloat($('.cart-totals ul li span')[1].innerText.substr(1));
			var total = subtotal + shipping;
			$('.cart-totals ul li span')[2].innerText ="$" + total.toFixed(2);
			$('.cart-totals ul li span')[3].innerText ="$" + total.toFixed(2);
		 });

		

        $('.cartHtml .input-counter').each(function() {
            var spinner = jQuery(this),
            input = spinner.find('input[type="text"]'),
            btnUp = spinner.find('.plus-btn'),
            btnDown = spinner.find('.minus-btn'),
            min = 0,
            max = 100;
			
            btnUp.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue >= max) {
					var newVal = oldValue;
				} 
				else {
					var newVal = oldValue + 1;
					var amount = newVal;
					var unit = this.parentNode.parentNode.previousSibling.previousSibling.children[0].innerText;
					var subtotal = this.parentNode.parentNode.nextSibling.nextSibling.children[0].innerText;
					subtotal = parseFloat(unit.substr(1)) * parseInt(amount);
					this.parentNode.parentNode.nextSibling.nextSibling.children[0].innerText ="$" + subtotal.toFixed(2);

					var table = $('.table.table-bordered tbody')[0];
					var sum = 0;
					for(var i=0;i<table.children.length;i++){
						sum += parseFloat(table.children[i].children[4].innerText.substr(1));
					}
					$('.cart-totals li:first-child span')[0].innerText = "$" + sum.toFixed(2);

					var subtotal = parseFloat($('.cart-totals ul li span')[0].innerText.substr(1));
					var shipping = parseFloat($('.cart-totals ul li span')[1].innerText.substr(1));
					var total = subtotal + shipping;
					$('.cart-totals ul li span')[2].innerText ="$" + total.toFixed(2);
					$('.cart-totals ul li span')[3].innerText ="$" + total.toFixed(2);

				}
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
            });
            btnDown.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue <= min) {
                    var newVal = oldValue;
				} 
				else {
					var newVal = oldValue - 1;
					var amount = newVal;
					var unit = this.parentNode.parentNode.previousSibling.previousSibling.children[0].innerText;
					var subtotal = this.parentNode.parentNode.nextSibling.nextSibling.children[0].innerText;
					subtotal = parseFloat(unit.substr(1)) * parseInt(amount);
					this.parentNode.parentNode.nextSibling.nextSibling.children[0].innerText ="$" + subtotal.toFixed(2);
					
					var table = $('.table.table-bordered tbody')[0];
					var sum = 0;
					for(var i=0;i<table.children.length;i++){
						sum += parseFloat(table.children[i].children[4].innerText.substr(1));
					}
					$('.cart-totals li:first-child span')[0].innerText ="$" + sum.toFixed(2);
					
					var subtotal = parseFloat($('.cart-totals ul li span')[0].innerText.substr(1));
					var shipping = parseFloat($('.cart-totals ul li span')[1].innerText.substr(1));
					var total = subtotal + shipping;
					$('.cart-totals ul li span')[2].innerText ="$" + total.toFixed(2);
					$('.cart-totals ul li span')[3].innerText ="$" + total.toFixed(2);
				}
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
			});
		});
		
		$('.product-quantities .input-counter').each(function() {
            var spinner = jQuery(this),
            input = spinner.find('input[type="text"]'),
            btnUp = spinner.find('.plus-btn'),
            btnDown = spinner.find('.minus-btn'),
            min = 0,
            max = 100;
			
            btnUp.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue >= max) {
					var newVal = oldValue;
				} 
				else {
					var newVal = oldValue + 1;
				}
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
            });
            btnDown.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue <= min) {
                    var newVal = oldValue;
				} 
				else {
					var newVal = oldValue - 1;
				}
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
			});
		});

        // Go to Top JS
		$(window).on('scroll', function() {
			var scrolled = $(window).scrollTop();
			if (scrolled > 600) $('.go-top').addClass('active');
			if (scrolled < 600) $('.go-top').removeClass('active');
		});  
		$('.go-top').on('click', function() {
			$("html, body").animate({ scrollTop: "0" },  500);
		});
		
		// Preloader
		jQuery(window).on('load', function() {
			$('.preloader').fadeOut()
		})

		
		$(".addCartWishlist").on('click',function(){
			var productName = this.parentNode.parentNode.children[2].innerText;
			var product_id = convertId(productName);
			$.post("./wishlist.html",{product_id:product_id, product_quantity:1},
				function(data){
						var href = "./cart.html";
						window.location.replace(href);
				}); 
		})

		$(".cart_item").on('click',function(){
			var product_id = parseInt(this.name);
			var new_path = "./wishlist.html";
			$.post(new_path,{product_id:product_id, product_quantity:1},
				function(data){
						var href = "./cart.html";
						window.location.replace(href);
				});  
		})

		$(".wishlist_item").on('click',function(){
			var product_id = parseInt(this.name);
			var new_path = "./addWishlist";
			$.post(new_path,{product_id:product_id},
				function(data){
						var href = "./wishlist.html";
						window.location.replace(href);
				});  
		})


		$(".delete").on('click', function(){
			var product_name = this.parentNode.parentNode.parentNode.children[2].innerText;
			var product_id = convertId(product_name);
			var new_path = "./removeWishlist";
			$.post(new_path,{product_id:product_id},
				function(data){
						var href = "./wishlist.html";
						window.location.replace(href);
				}); 
		})


		$(".back").on('click', function(){
			window.location.replace("./index.html");
		})

		$(".product-detail-cart").on('click',function(){
			var product_name = $(".product-name").text();
			var product_quantity = parseInt($(".product-quantity").val());
			var product_id = convertId(product_name);
			console.log(product_id);
			console.log(product_name);
			console.log(product_quantity);
			var new_path = "./wishlist.html";
			$.post(new_path,{product_id:product_id, product_quantity:product_quantity},
				function(data){
						var href = "./cart.html";
						window.location.replace(href);
				});  
		})

		$(".checkDetails").on('click', function(){
			var order_id = this.parentNode.parentNode.children[0].innerText;
			console.log(order_id);
			var new_path = './orderDetail' + order_id;
			window.location.replace(new_path); 
		})

		$("#backHome").on('click', function(event){
			event.preventDefault();
			var new_path = './index.html';
			window.location.replace(new_path); 
		})


}(jQuery));

