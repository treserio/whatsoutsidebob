"use strict";
function showColors() {
    var fc = document.getElementById('filter-colors');
    if (fc.checked) {
        document.getElementById('filter-subjects').checked = false;
        document.getElementById('list-subjects').style.display = 'none';
        document.getElementById('list-colors').style.display = 'flex';
    }
    else {
        document.getElementById('list-colors').style.display = 'none';
    }
}
function showSubjects() {
    var fs = document.getElementById('filter-subjects');
    if (fs.checked) {
        document.getElementById('filter-colors').checked = false;
        document.getElementById('list-colors').style.display = 'none';
        document.getElementById('list-subjects').style.display = 'flex';
    }
    else {
        document.getElementById('list-subjects').style.display = 'none';
    }
}
