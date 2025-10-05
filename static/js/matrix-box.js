document.querySelectorAll('.matrix-card').forEach(card => {
  card.addEventListener('click', function () {
    // Get the index from the preview section
    const preview = this.querySelector('.matrix-preview');
    const index = preview.getAttribute('data-details');

    // Get the hidden details content
    const details = document.querySelector(`#details-${index}`);
    const modalDetails = document.querySelector('#modal-details');
    const modal = document.querySelector('#matrix-modal');

    if (details && modalDetails && modal) {
      modalDetails.innerHTML = details.innerHTML;
      modal.style.display = 'flex';
    }
  });
});

// Close modal when clicking the close button
document.querySelector('.close-modal').addEventListener('click', function () {
  document.querySelector('#matrix-modal').style.display = 'none';
});

// Close modal when clicking outside the modal content
window.addEventListener('click', function (event) {
  const modal = document.querySelector('#matrix-modal');
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});