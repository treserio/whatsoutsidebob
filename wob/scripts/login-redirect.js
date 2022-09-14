"use strict";
// need to check for special chars in auth-token!!! & fix regex if needed
// document.cookie = "Authorization=Token FAILED"
// dfcf19a03c33d4e3a5661e61e944c783cc1ad3d4
var loginAuthCheck = function () {
    // grab our authorization string from the cookie to add to the header
    var authMatch = document.cookie.match(/Authorization=(Token [\w\d]+)/);
    if (!authMatch || !authMatch[1]) {
        // need to make sure the document is ready
        setTimeout(function () {
            var _a;
            document.querySelector("body").style.visibility = "visible";
            (_a = document.querySelector("#loader")) === null || _a === void 0 ? void 0 : _a.remove();
        }, 300);
        return;
    }
    var Authorization = authMatch[1];
    // console.log('auth', {Authorization});
    fetch('http://localhost:8000/api/all_info/', {
        headers: { Authorization: Authorization }
    })
        .then(function (res) {
        var _a;
        // console.log('res', res);
        // console.log('status:', res.status);
        if (res.status == 200) {
            window.location.replace('http://127.0.0.1:5500/wob/templates/app.html');
        }
        else {
            // remove the cookie and load fix the visibility
            document.cookie = "Authorization=Token Failed; expires=Sat, 01 Jan 2022 00:00:01 GMT";
            document.querySelector("body").style.visibility = "visible";
            (_a = document.querySelector("#loader")) === null || _a === void 0 ? void 0 : _a.remove();
        }
    });
};
loginAuthCheck();
// script on form submit
setTimeout(function () {
    var login = document.querySelector('#login');
    // console.log(login);
    if (login) {
        login.onsubmit = function (e) {
            // console.log(e);
            if (e && e.target && e.target[0] && e.target[1]) {
                // console.log(e.target[0].value)
                // console.log(e.target[1].value)
                checkLogin(e.target[0].value, e.target[1].value);
            }
            return false;
        };
    }
}, 250);
function checkLogin(username, password) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8000/api/login/', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            // console.log(json);
            // console.log(json.token);
            document.cookie = "Authorization=Token ".concat(json.token, "; SameSite=None; Secure");
            window.location.replace('http://127.0.0.1:5500/wob/templates/app.html');
        }
    };
    xhr.send(JSON.stringify({ username: username, password: password }));
}
