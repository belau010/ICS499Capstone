<script>
  import axios from "axios";

  // @ts-nocheck

  let email = "";
  let password = "";
  let verifyPassword = "";
  let firstName = "";
  let lastName = "";

  function onEmailInput(event) {
    email = event.target.value;
  }

  function onPasswordInput(event) {
    password = event.target.value;
  }

  function onVerifyPasswordInput(event) {
    verifyPassword = event.target.value;
  }

  function onFirstNameInput(event) {
    firstName = event.target.value;
  }

  function onLastNameInput(event) {
    lastName = event.target.value;
  }

  function onRegisterClick() {
    axios.post("http://127.0.0.1:5000/user/register", {email, firstName, lastName, password})
  }
</script>

<main>
  <div id="register-container">
    <input
      type="text"
      placeholder="E-mail Address"
      value={email}
      on:input={onEmailInput}
    />
    <br />
    <input
      type="text"
      placeholder="First Name"
      value={firstName}
      on:input={onFirstNameInput}
    />
    <br />
    <input
      type="text"
      placeholder="Last Name"
      value={lastName}
      on:input={onLastNameInput}
    />
    <br />
    <input
      type="password"
      placeholder="Password"
      value={password}
      on:input={onPasswordInput}
    />
    <br />
    <input
      type="password"
      placeholder="Verify Password"
      value={verifyPassword}
      on:input={onVerifyPasswordInput}
    />
    <br />
    <button on:click={onRegisterClick}>
      Register
    </button>
  </div>
</main>

<style>
  #register-container {
    padding: 16px;
  }
</style>
