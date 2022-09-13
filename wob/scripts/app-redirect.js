// need to check for special chars in auth-token!!! & fix regex if needed
// document.cookie = "Authorization=Token Failed"
// dfcf19a03c33d4e3a5661e61e944c783cc1ad3d4
authCheck();
function authCheck() {
  // grab our authorization string from the cookie to add to the header
  let Authorization = document.cookie.match(/Authorization=(Token [\w\d]+)/);
  if (!Authorization) {
    window.location.replace('http://127.0.0.1:5500/wob/templates/');
  }
  Authorization = Authorization[1];
  console.log('auth', {Authorization});
  fetch('http://localhost:8000/api/all_info/', {
    headers: {Authorization}
  })
    .then((res) => {
      // console.log('res', res);
      // console.log('status:', res.status);
      if (res.status == 200) {
        // user is authorized, correct visibility
        document.querySelector("body").style.visibility = "visible";
        document.querySelector("#loader").remove();
      } else {
        // remove the cookie and redirect
        document.cookie = "Authorization=Token Failed; expires=Sat, 01 Jan 2022 00:00:01 GMT";
        window.location.replace('http://127.0.0.1:5500/wob/templates/');
      }
    });
}


