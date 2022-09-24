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

// function for populating color filter list
(() => {
    // grab our authorization string from the cookie to add to the header
    const authMatch = document.cookie.match(/Authorization=(Token [\w\d]+)/);
    const Authorization: string | null = authMatch![1];
    // grab our color values to use for filters
    fetch('http://localhost:8000/api/hex_values/', {
        headers: {Authorization}
    })
        .then((res) => {
            res.json()
                .then((data) => {
                    for (let index = 0; index < data.count; ) {
                        const tripleFrag = document.createDocumentFragment();
                        for (let i = 0; i < 3; ++i, ++index) {
                            const wrapFrag = document.createDocumentFragment();
                            const entry = data.results[index];
                            const checkbox = <HTMLInputElement> document.createElement('input');
                            checkbox.name = `option-c${index}`;
                            checkbox.id = `option-c${index}`;
                            checkbox.type = 'checkbox';
                            // example option for filter for all_info endpoint
                            // episode_colors__alizarin_crimson=1
                            checkbox.value = 'episode_colors__' + entry.color.toLowerCase().split(' ').join('_') + '=1';
                            const label = <HTMLLabelElement> document.createElement('label');
                            label.setAttribute('style', `background-color: ${entry.hex}; border: 4px solid ${entry.hex}`);
                            label.htmlFor = `option-c${index}`;
                            label.className = 'rounded-full border-4 px-2 py-1 whitespace-nowrap';
                            label.innerHTML = entry.color;
                            // append fragments to div
                            wrapFrag.appendChild(checkbox);
                            wrapFrag.appendChild(label);
                            const wrap = document.createElement('div');
                            tripleFrag.append(wrap);
                            wrap.appendChild(wrapFrag);
                        }
                        const threeColors = document.createElement('div');
                        threeColors.className = 'flex justify-around my-3 md:w-1/2';
                        threeColors.appendChild(tripleFrag);
                        document.getElementById('append-colors-here')?.append(threeColors);
                    }
                });
        })
        .catch((err) => {
            console.log('err', err);
        });
    // now grab our list of subjects
    fetch('http://localhost:8000/api/subjects/?episode=S01E01', {
        headers: {Authorization}
    })
        .then((res) => {
            res.json()
                .then((data) => {
                    // console.log(data);
                    const subjects = Object.keys(data.results[0]).slice(1);
                    // console.log(subjects);
                    for (let index = 0; index < subjects.length; ++index) {
                        const tripleFrag = document.createDocumentFragment();
                        for (let i = 0; i < 3; ++i, ++index) {
                            const wrapFrag = document.createDocumentFragment();
                            const checkbox = <HTMLInputElement> document.createElement('input');
                            checkbox.name = `option-s${index}`;
                            checkbox.id = `option-s${index}`;
                            checkbox.type = 'checkbox';
                            // episode_subjects__aurora_borealis=0
                            checkbox.value = 'episode_colors__' + subjects[index] + '=1';
                            const label = <HTMLLabelElement> document.createElement('label');
                            label.htmlFor = `option-s${index}`;
                            label.className = 'rounded-full bg-black border-4 border-black px-2 py-1 whitespace-nowrap';
                            // because it looks better when things are capitalized on the first letters
                            let subjString = subjects[index].split('_');
                            for (let j = 0; j < subjString.length; ++j) {
                                let firstLetter = subjString[j].charAt(0);
                                subjString[j] = firstLetter.toUpperCase() + subjString[j].slice(1);
                            }
                            label.innerHTML = subjString.join(' ');
                            // append fragments to div
                            wrapFrag.appendChild(checkbox);
                            wrapFrag.appendChild(label);
                            const wrap = document.createElement('div');
                            tripleFrag.append(wrap);
                            wrap.appendChild(wrapFrag);
                        }
                        const threeColors = document.createElement('div');
                        threeColors.className = 'flex justify-around my-3 md:w-1/2';
                        threeColors.appendChild(tripleFrag);
                        document.getElementById('append-subjects-here')?.append(threeColors);
                    }
                });
        })
        .catch((err) => {
            console.log('err', err);
        });
    // may need to wait for fetch so page can draw?
    var appendHere = <HTMLInputElement> document.getElementById('append-colors-here');
})()
