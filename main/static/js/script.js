if ($(window).width() < 960) {
    $(".baner_img_1").attr("src", "/main/static/img/baner4_mobile.png");
    $(".baner_img_2").attr("src", "/main/static/img/baner2_mobile.png");
    $(".baner_img_3").attr("src", "/main/static/img/baner3_mobile.png");
 }

$(".slider_item").click(function(){
    var img_url = $(this).find(".slider_img").attr("src");
    $(this).siblings().removeClass("slider_item_active");
    $(this).addClass("slider_item_active");
    $(".product_img").attr("src", img_url);
    $(".img_link").attr("href", img_url);
})

$('.img_link').magnificPopup({
    type: 'image'
    // other options
  });

$(".burger_menu_icon").click(function(){
    $(this).toggleClass('open');
    $(".burger_menu").toggleClass("burger_menu_active");
    $(".menu_mobile").toggleClass("menu_mobile_burger_active");
})

$(".review").slice(0, 5).show();
if($(".review:hidden").length == 0){
    $(".load_more_btn").fadeOut();
}

$(".load_more_btn").click(function(){
    $(".review:hidden").slice(0, 5).show();

    if($(".review:hidden").length == 0){
        $(".load_more_btn").hide();
    }
});

$(".user_review").slice(0, 5).show();
if($(".user_review:hidden").length == 0){
    $(".user_reviews_load_more_btn").fadeOut();
}

$(".user_reviews_load_more_btn").click(function(){
    $(".user_review:hidden").slice(0, 5).show();

    if($(".user_review:hidden").length == 0){
        $(".user_reviews_load_more_btn").hide();
    }
});

$(".order").slice(0, 5).css("display","flex");
if($(".order:hidden").length == 0){
    $(".user_orders_load_more_btn").fadeOut();
}

$(".user_orders_load_more_btn").click(function(){
    $(".order:hidden").slice(0, 5).css("display","flex");

    if($(".order:hidden").length == 0){
        $(".user_orders_load_more_btn").hide();
    }
});

$(".search_activator").click(function(){
    $(".menu_link").addClass("menu_link_hidden");
    $(".search_header").addClass("search_header_active");
    $(".search_deactivator").addClass("search_deactivator_active");
});
$(".search_deactivator").click(function(){
    $(".menu_link").removeClass("menu_link_hidden");
    $(".search_header").removeClass("search_header_active");
    $(this).removeClass("search_deactivator_active");
});

$(".search_activator_mobile").click(function(){
    $(".logo_name").addClass("hidden");
    $(".search_activator_mobile").addClass("hidden");
    $(".burger_menu_icon").addClass("hidden");
    $(".search_header").addClass("search_header_active");
    $(".search_deactivator_mobile").addClass("search_deactivator_active");
});

$(".search_deactivator_mobile").click(function(){
    $(".logo_name").removeClass("hidden");
    $(".search_activator_mobile").removeClass("hidden");
    $(".burger_menu_icon").removeClass("hidden");
    $(".search_header").removeClass("search_header_active");
    $(this).removeClass("search_deactivator_active");
});

$(".add_cart_day").click(function(){

    $(this).addClass("add_cart_inactive");
    $(this).find("p").html("В корзине");

    var prod_id = $(".product_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
        method: "POST",
        url: "/cart/cart_add/",
        data: {
            product_id: prod_id,
            rental_time: 1,
            csrfmiddlewaretoken: token,
        }
    });
});
$(".add_cart_week").click(function(){

    $(this).addClass("add_cart_inactive");
    $(this).find("p").html("В корзине");

    $(".order_button").addClass("add_cart_inactive");
    $(".order_button").find("p").html("В корзине");

    var prod_id = $(".product_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
        method: "POST",
        url: "/cart/cart_add/",
        data: {
            product_id: prod_id,
            rental_time: 7,
            csrfmiddlewaretoken: token,
        }
    });
});
$(".cart_delete_js").click(function(){

    var prod_id = $(this).parent().find(".game_id_ajax").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
        method: "POST",
        url: "/cart/delete/",
        data: {
            product_id: prod_id,
            csrfmiddlewaretoken: token,
        },
    });

    window.location.href = "/cart/";

});

$(".pickup_btn").click(function(){
    $(this).siblings().removeClass("submit_choose_method_btn_active");
    $(this).toggleClass("submit_choose_method_btn_active");
    $(".choose_delivery_method_warning").addClass("hidden");

    if($(".pickup_fields_container").hasClass("hidden")){
        $(".delivery_fields_container").addClass("hidden");
        $(".delivery_warning").addClass("hidden");
        $(".pickup_fields_container").removeClass("hidden");
    }

    $(".delivery_method_js").html(" Самовывоз");
});
$(".delivery_btn").click(function(){
    $(this).siblings().removeClass("submit_choose_method_btn_active");
    $(this).toggleClass("submit_choose_method_btn_active");
    $(".choose_delivery_method_warning").addClass("hidden");

    $(".delivery_fields_container").toggleClass("hidden");
    $(".pickup_fields_container").toggleClass("hidden");
    $(".delivery_warning").toggleClass("hidden");

    $(".delivery_method_js").html(" Доставка");
});

$(".cash_btn").click(function(){
    $(this).siblings().removeClass("submit_choose_method_btn_active");
    $(this).toggleClass("submit_choose_method_btn_active");
    $(".choose_pay_method_warning").addClass("hidden");

    $(".cash_warning").toggleClass("hidden");

    $(".payment_method_js").html(" Наличные");
});
$(".card_btn").click(function(){
    $(this).siblings().removeClass("submit_choose_method_btn_active");
    $(this).toggleClass("submit_choose_method_btn_active");
    $(".choose_pay_method_warning").addClass("hidden");

    $(".cash_warning").addClass("hidden");

    $(".payment_method_js").html(" Банковская карта");
});

$(".cart_buy_btn").click(function(){
    var payment_method = $(".payment_method_js").text();
    var delivery_method = $(".delivery_method_js").text();
    var user_adress = $(".user_adress_input").val();

    let games_ids = $(".games_ids").val();
    var total_price = $(".cart_submit_total_price").text();
    var total_items = $(".total_items_js").text();

    prod_ids_json = JSON.stringify(games_ids);
    var token = $("input[name=csrfmiddlewaretoken]").val();

    if (payment_method != ""){
        if (delivery_method != ""){
            if (payment_method == " Наличные" && delivery_method == " Доставка")
            {
                $(".cash_warning").html("Оплата Наличными возможна только при Самовывозе!");
            }
            else if(payment_method == " Наличные" && delivery_method == " Самовывоз")
            {
                $.ajax({
                    method: "POST",
                    url: "/update_availability/",
                    data: {
                        product_ids: prod_ids_json,
                        get_order_method: delivery_method,
                        payment_method: payment_method,
                        total_price: total_price,
                        adress: user_adress,
                        csrfmiddlewaretoken: token,
                    },
                    success: function(data) {
                        window.location.href = data;
                     },
                });        
            }
            else if(payment_method == " Банковская карта" && delivery_method == " Доставка" && user_adress != "")
            {
                $.ajax({
                    method: "POST",
                    url: "/pay_bill/",
                    data: {
                        product_ids: prod_ids_json,
                        get_order_method: delivery_method,
                        payment_method: payment_method,
                        total_price: total_price,
                        adress: user_adress,
                        csrfmiddlewaretoken: token,
                    },
                    success: function(data) {
                        window.location.href = data;
                     },
                });
            }
            else if(payment_method == " Банковская карта" && delivery_method == " Доставка" && user_adress == "")
            {
                $(".adress_is_empty_warning").removeClass("hidden");
            }
            else if(payment_method == " Банковская карта" && delivery_method == " Самовывоз")
            {
                $.ajax({
                    method: "POST",
                    url: "/pay_bill/",
                    data: {
                        product_ids: prod_ids_json,
                        get_order_method: delivery_method,
                        payment_method: payment_method,
                        total_price: total_price,
                        adress: user_adress,
                        csrfmiddlewaretoken: token,
                    },
                    success: function(data) {
                        window.location.href = data;
                     },
                });
            }
        }else{
            $(".choose_delivery_method_warning").removeClass("hidden");
        }
    }else{
        $(".choose_pay_method_warning").removeClass("hidden");
    }

});
$(".baners_slider").slick({
    infinite: true,
    dots: true,
    autoplay: true,
    autoplaySpeed: 3000,
});