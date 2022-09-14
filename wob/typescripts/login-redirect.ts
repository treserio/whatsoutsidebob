// need to check for special chars in auth-token!!! & fix regex if needed
// document.cookie = "Authorization=Token FAILED"
// dfcf19a03c33d4e3a5661e61e944c783cc1ad3d4
const loginAuth = (): void => {
  // grab our authorization string from the cookie to add to the header
  const authMatch = document.cookie.match(/Authorization=(Token [\w\d]+)/);
  if (!authMatch || !authMatch[1]) {
    // need to make sure the document is ready
    setTimeout(() => {
      document.querySelector("body")!.style.visibility = "visible";
      document.querySelector("#loader")?.remove();
    }, 300);
    return;
  }
  const Authorization: string | null = authMatch[1];
  // console.log('auth', {Authorization});
  fetch('http://localhost:8000/api/all_info/', {
    headers: {Authorization}
  })
    .then((res) => {
      // console.log('res', res);
      // console.log('status:', res.status);
      if (res.status == 200) {
        window.location.replace('http://127.0.0.1:5500/wob/templates/app.html');
      } else {
        // remove the cookie and load fix the visibility
        document.cookie = "Authorization=Token Failed; expires=Sat, 01 Jan 2022 00:00:01 GMT";
        document.querySelector("body")!.style.visibility = "visible";
        document.querySelector("#loader")?.remove();
      }
    });
}
loginAuth();
