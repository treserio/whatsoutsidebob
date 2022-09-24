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
// function for populating color filter list
(function () {
    // grab our authorization string from the cookie to add to the header
    var authMatch = document.cookie.match(/Authorization=(Token [\w\d]+)/);
    var Authorization = authMatch[1];
    // grab our color values to use for filters
    fetch('http://localhost:8000/api/hex_values/', {
        headers: { Authorization: Authorization }
    })
        .then(function (res) {
        res.json()
            .then(function (data) {
            var _a;
            for (var index = 0; index < data.count;) {
                var tripleFrag = document.createDocumentFragment();
                for (var i = 0; i < 3; ++i, ++index) {
                    var wrapFrag = document.createDocumentFragment();
                    var entry = data.results[index];
                    var checkbox = document.createElement('input');
                    checkbox.name = "option-c".concat(index);
                    checkbox.id = "option-c".concat(index);
                    checkbox.type = 'checkbox';
                    // example option for filter for all_info endpoint
                    // episode_colors__alizarin_crimson=1
                    checkbox.value = 'episode_colors__' + entry.color.toLowerCase().split(' ').join('_') + '=1';
                    var label = document.createElement('label');
                    label.setAttribute('style', "background-color: ".concat(entry.hex, "; border: 4px solid ").concat(entry.hex));
                    label.htmlFor = "option-c".concat(index);
                    label.className = 'rounded-full border-4 px-2 py-1 whitespace-nowrap';
                    label.innerHTML = entry.color;
                    // append fragments to div
                    wrapFrag.appendChild(checkbox);
                    wrapFrag.appendChild(label);
                    var wrap = document.createElement('div');
                    tripleFrag.append(wrap);
                    wrap.appendChild(wrapFrag);
                }
                var threeColors = document.createElement('div');
                threeColors.className = 'flex justify-around my-3 md:w-1/2';
                threeColors.appendChild(tripleFrag);
                (_a = document.getElementById('append-colors-here')) === null || _a === void 0 ? void 0 : _a.append(threeColors);
            }
        });
    })
        .catch(function (err) {
        console.log('err', err);
    });
    // now grab our list of subjects
    fetch('http://localhost:8000/api/subjects/?episode=S01E01', {
        headers: { Authorization: Authorization }
    })
        .then(function (res) {
        res.json()
            .then(function (data) {
            var _a;
            // console.log(data);
            var subjects = Object.keys(data.results[0]).slice(1);
            // console.log(subjects);
            for (var index = 0; index < subjects.length; ++index) {
                var tripleFrag = document.createDocumentFragment();
                for (var i = 0; i < 3; ++i, ++index) {
                    var wrapFrag = document.createDocumentFragment();
                    var checkbox = document.createElement('input');
                    checkbox.name = "option-s".concat(index);
                    checkbox.id = "option-s".concat(index);
                    checkbox.type = 'checkbox';
                    // episode_subjects__aurora_borealis=0
                    checkbox.value = 'episode_colors__' + subjects[index] + '=1';
                    var label = document.createElement('label');
                    label.htmlFor = "option-s".concat(index);
                    label.className = 'rounded-full bg-black border-4 border-black px-2 py-1 whitespace-nowrap';
                    // because it looks better when things are capitalized on the first letters
                    var subjString = subjects[index].split('_');
                    for (var j = 0; j < subjString.length; ++j) {
                        var firstLetter = subjString[j].charAt(0);
                        subjString[j] = firstLetter.toUpperCase() + subjString[j].slice(1);
                    }
                    label.innerHTML = subjString.join(' ');
                    // append fragments to div
                    wrapFrag.appendChild(checkbox);
                    wrapFrag.appendChild(label);
                    var wrap = document.createElement('div');
                    tripleFrag.append(wrap);
                    wrap.appendChild(wrapFrag);
                }
                var threeColors = document.createElement('div');
                threeColors.className = 'flex justify-around my-3 md:w-1/2';
                threeColors.appendChild(tripleFrag);
                (_a = document.getElementById('append-subjects-here')) === null || _a === void 0 ? void 0 : _a.append(threeColors);
            }
        });
    })
        .catch(function (err) {
        console.log('err', err);
    });
    // may need to wait for fetch so page can draw?
    var appendHere = document.getElementById('append-colors-here');
})();
