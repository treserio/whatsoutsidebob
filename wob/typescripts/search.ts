function showColors() {
    var fc = <HTMLInputElement> document.getElementById('filter-colors');
    if (fc.checked) {
        (<HTMLInputElement> document.getElementById('filter-subjects')).checked = false;
        document.getElementById('list-subjects')!.style.display = 'none';
        document.getElementById('list-colors')!.style.display = 'flex';
    } else {
        document.getElementById('list-colors')!.style.display = 'none';
    }
}

function showSubjects() {
    var fs = <HTMLInputElement> document.getElementById('filter-subjects');
    if (fs.checked) {
        (<HTMLInputElement> document.getElementById('filter-colors')).checked = false;
        document.getElementById('list-colors')!.style.display = 'none';
        document.getElementById('list-subjects')!.style.display = 'flex';
    } else {
        document.getElementById('list-subjects')!.style.display = 'none';
    }
}

