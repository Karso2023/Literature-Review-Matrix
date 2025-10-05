document.querySelectorAll('.delete-btn').forEach(btn => {
  btn.addEventListener('click', function (e) {
    e.stopPropagation(); 

    const matrixId = this.dataset.id;
    const confirmed = confirm("Are you sure you want to delete this matrix?");
    if (confirmed) {
      fetch('/delete', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({ id: matrixId })
      })
      .then(response => {
        if (response.ok) {
          this.closest('.matrix-card').remove(); 
        } else {
          alert("Failed to delete matrix.");
        }
      });
    }
  });
});
