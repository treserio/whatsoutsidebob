"use strict";
var modalToggle = function () {
    var openButton = document.getElementById('modalOpen');
    var modal = document.getElementById('authentication-modal');
    var closeButton = document.getElementById('modalClose');
    var closeButton2 = document.getElementById('modalClose2');
    openButton === null || openButton === void 0 ? void 0 : openButton.addEventListener('click', function () {
        modal === null || modal === void 0 ? void 0 : modal.classList.remove('hidden');
        modal === null || modal === void 0 ? void 0 : modal.classList.add('animate__fadeInDown');
    });
    closeButton === null || closeButton === void 0 ? void 0 : closeButton.addEventListener('click', function () {
        modal === null || modal === void 0 ? void 0 : modal.classList.remove('animate__fadeInDown');
        modal === null || modal === void 0 ? void 0 : modal.classList.add('hidden');
    });
    closeButton2 === null || closeButton2 === void 0 ? void 0 : closeButton2.addEventListener('click', function () {
        modal === null || modal === void 0 ? void 0 : modal.classList.remove('animate__fadeInDown');
        modal === null || modal === void 0 ? void 0 : modal.classList.add('hidden');
    });
};
var pwdConfirm = function () {
    var password = (document.querySelector('input[name=newPassword]'));
    var confirm = (document.querySelector('input[name=confirm]'));
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
    }
    else {
        confirm.setCustomValidity('Passwords do not match');
    }
};
var createNewUser = function () {
    var form = document.querySelector('#modalForm');
    if (form) {
        form.onsubmit = function (e) {
            e.preventDefault();
            var username = e.target[0].value;
            var firstname = e.target[1].value;
            var lastname = e.target[2].value;
            var email = e.target[3].value;
            var password = e.target[4].value;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost:8000/api/register/', true);
            xhr.setRequestHeader('Accept', 'application/json');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function () {
                console.log('👁👅👁');
                if (xhr.status === 200 && xhr.readyState === 4) {
                    var modal = document.getElementById('authentication-modal');
                    modal === null || modal === void 0 ? void 0 : modal.classList.toggle('hidden');
                    document.forms[1].reset();
                }
                else if (xhr.readyState === 4) {
                    var username_1 = document.getElementById('newUsername');
                    var usernameInUse = document.getElementById('inUse');
                    username_1 === null || username_1 === void 0 ? void 0 : username_1.classList.add('border-4');
                    username_1 === null || username_1 === void 0 ? void 0 : username_1.classList.add('border-red-500');
                    usernameInUse === null || usernameInUse === void 0 ? void 0 : usernameInUse.classList.remove('hidden');
                }
            };
            var data = JSON.stringify({
                username: username,
                firstname: firstname,
                lastname: lastname,
                email: email,
                password: password
            });
            xhr.send(data);
        };
    }
    return false;
};
window.addEventListener('load', function () {
    modalToggle();
    createNewUser();
});
