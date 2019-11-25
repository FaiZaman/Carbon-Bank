$(document).ready(function(){
    $(".xx-report").hide();
    $(".transport-report").hide();
    $(".food-report").hide();
    $(".living-report").hide();

    

// jQuery methods go here...
    $(".fuel-card, .transport-card, .food-card, .living-card").click(function(){
        $(".card-row").hide();
        $(".xx-report").show();
    });
});