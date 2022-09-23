function showColors() {
  var fc = document.getElementById('filter_colors');
  if (fc.checked) {
    document.getElementById('list_colors').style.display = 'flex';
  } else {
    document.getElementById('list_colors').style.display = 'none';
  }
}

function showSubjects() {
  var fc = document.getElementById('filter_subjects');
  if (fc.checked) {
    document.getElementById('list_subjects').style.display = 'flex';
  } else {
    document.getElementById('list_subjects').style.display = 'none';
  }
}
