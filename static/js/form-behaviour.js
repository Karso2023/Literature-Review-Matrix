// Just a small function for how the review matrix is shown

$(document).ready(function() {
  let currentSection = "#first-section"; 
  
  $(".next-btn").on("click", function() {
    const nextSection = $(this).data("next");
    $(this).closest(".section").hide();
    $(nextSection).show();
    currentSection = nextSection; 
  });

  $("#view-all").on("change", function() {
    if ($(this).is(":checked")) {
      $(".section").show();
      $(".next-btn").hide();
    } else {
      $(".section").hide();
      $(currentSection).show();
      $(".next-btn").show();
    }
  });
});
