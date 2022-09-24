const modalToggle = () => {
  const openButton = document.getElementById('modalOpen');
  const modal = document.getElementById('authentication-modal');
  const closeButton = document.getElementById('modalClose');
  const closeButton2 = document.getElementById('modalClose2');

  openButton?.addEventListener('click', () => {
    modal?.classList.remove('hidden');
    modal?.classList.add('animate__fadeInDown');
  });

  closeButton?.addEventListener('click', () => {
    modal?.classList.remove('animate__fadeInDown');
    modal?.classList.add('hidden');
  });

  closeButton2?.addEventListener('click', () => {
    modal?.classList.remove('animate__fadeInDown');
    modal?.classList.add('hidden');
  });
};

const pwdConfirm = () => {
  const password = <HTMLSelectElement>(
    document.querySelector('input[name=newPassword]')
  );
  const confirm = <HTMLSelectElement>(
    document.querySelector('input[name=confirm]')
  );
  if (confirm.value === password.value) {
    confirm.setCustomValidity('');
  } else {
    confirm.setCustomValidity('Passwords do not match');
  }
};

const createNewUser = () => {
  const form: HTMLFormElement | null = document.querySelector('#modalForm');

  if (form) {
    form.onsubmit = (e: any) => {
      e.preventDefault();
      let username = e.target[0].value;
      let firstname = e.target[1].value;
      let lastname = e.target[2].value;
      let email = e.target[3].value;
      let password = e.target[4].value;

      let xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://localhost:8000/api/register/', true);
      xhr.setRequestHeader('Accept', 'application/json');
      xhr.setRequestHeader('Content-Type', 'application/json');

      xhr.onreadystatechange = function () {
        console.log('👁👅👁');
        if (xhr.status === 200 && xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
        } else if (xhr.readyState === 4) {
          alert(
            'Username already exists, please login or try another username'
          );
        }
      };

      let data = JSON.stringify({
        username: username,
        firstname: firstname,
        lastname: lastname,
        email: email,
        password: password
      });

      xhr.send(data);
      const modal = document.getElementById('authentication-modal');
      modal?.classList.toggle('hidden');
      document.forms[1].reset();
    };
  }
  return false;
};

window.addEventListener('load', () => {
  modalToggle();
  createNewUser();
});
