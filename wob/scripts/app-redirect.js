"use strict";
// need to check for special chars in auth-token!!! & fix regex if needed
// document.cookie = "Authorization=Token Failed"
// dfcf19a03c33d4e3a5661e61e944c783cc1ad3d4
var appAuth = function () {
    // grab our authorization string from the cookie to add to the header
    var authMatch = document.cookie.match(/Authorization=(Token [\w\d]+)/);
    if (!authMatch || !authMatch[1]) {
        window.location.replace('http://127.0.0.1:5500/wob/templates/');
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
            // user is authorized, correct visibility
            document.querySelector("body").style.visibility = "visible";
            (_a = document.querySelector("#loader")) === null || _a === void 0 ? void 0 : _a.remove();
        }
        else {
            // remove the cookie and redirect
            document.cookie = "Authorization=Token Failed; expires=Sat, 01 Jan 2022 00:00:01 GMT";
            window.location.replace('http://127.0.0.1:5500/wob/templates/');
        }
    });
};
appAuth();
