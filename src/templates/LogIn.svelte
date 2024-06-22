<script>
  import axios from "axios";
  export let setView;

  // @ts-nocheck

  let email = "";
  let password = "";

  function onEmailInput(event) {
    email = event.target.value;
  }

  function onPasswordInput(event) {
    password = event.target.value;
  }

  function onLogInClick() {
    axios
      .post("http://127.0.0.1:5000/user/logIn", { email, password })
      .then((response) => {
        if (response.data.success) {
          setView("dashboard");
        } else {
          alert("Log in failed: " + response.data.message);
        }
      });
  }

  function onCreateAccountClick() {
    setView("register");
  }
</script>

<main>
  <div id="log-in-container">
    <input
      type="text"
      placeholder="E-mail Address"
      value={email}
      on:input={onEmailInput}
    />
    <br />
    <input
      type="password"
      placeholder="Password"
      value={password}
      on:input={onPasswordInput}
    />
    <br />
    <button on:click={onLogInClick}> Log In </button>
    <br />
    <button on:click={onCreateAccountClick}> Create Account </button>
  </div>
</main>

<style>
  #log-in-container {
    padding: 16px;
  }
</style>
