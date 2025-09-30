// Just a small function for how the review matrix is shown with some error handlings

$(document).ready(function () {
  let currentSection = "#first-section";

  function clearError(input) {
    input.removeClass("input-error");
    input.next(".error-message").remove();
  }

  function showError(input, message) {
    clearError(input);
    input.addClass("input-error");
    input.after(`<div class="error-message" style="color:red; font-size:0.9em; margin-top:4px;">${message}</div>`);
  }

  $(".next-btn").on("click", function () {
    const nextSection = $(this).data("next");
    const yearInput = $("#year");
    const yearValue = parseInt(yearInput.val(), 10);
    const minYear = parseInt(yearInput.attr("min"), 10);
    const maxYear = parseInt(yearInput.attr("max"), 10);

    clearError(yearInput);

    if (isNaN(yearValue) || yearValue < minYear || yearValue > maxYear) {
      showError(yearInput, `Please enter a valid year between ${minYear} and ${maxYear}.`);
      yearInput.focus();
      return;
    }

    $(this).closest(".section").hide();
    $(nextSection).show();
    currentSection = nextSection;
  });

  $(".useful-btn").on("click", function () {
    const response = $(this).data("response");
    const nextSection = $(this).data("next");
    const parentSection = $(this).closest(".section");

    parentSection.hide();

    if (response === "yes" && nextSection) {
      $(nextSection).show();
      currentSection = nextSection;
    } else {
      $("#third-pass").hide(); 
      if ($("#final-submit").length === 0) {
        $("<div id='final-submit' style='text-align:center; margin-top:20px;'><button type='submit'>Submit Review Matrix</button></div>").insertAfter(parentSection);
      }
    }
  });

  $("#view-all").on("change", function () {
    if ($(this).is(":checked")) {
      $(".section").show();
      $(".next-btn, .useful-btn").hide();
    } else {
      $(".section").hide();
      $(currentSection).show();
      $(".next-btn, .useful-btn").show();
    }
  });
});

document.querySelector('form').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    const thirdPassVisible = document.querySelector('#third-pass').style.display !== 'none';
    if (!thirdPassVisible) {
      event.preventDefault(); // Stop form submission
    }
  }
});
