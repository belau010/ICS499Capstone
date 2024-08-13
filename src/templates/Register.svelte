<script>
// @ts-nocheck

  import { currentView } from "../state";
  import API from "../API";
  import { onMount } from "svelte";

  // @ts-nocheck

  let email = "";
  let password = "";
  let verifyPassword = "";
  let firstName = "";
  let lastName = "";
  let payRate = 15.0;
  let position = "associate";
  let forcePasswordChange = true;
  let registerButton = null;

  onMount(() => {
    registerButton = document.getElementById("register-button");
  });

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

  async function onRegisterClick() {
    if (password != verifyPassword){
      alert("Passwords do not match")
      return 
    }
    registerButton.disabled = true;
    await API.user.register(
      email,
      firstName,
      lastName,
      password,
      payRate,
      position,
      forcePasswordChange
    );
    registerButton.disabled = false;
    email = "";
    password = "";
    verifyPassword = "";
    firstName = "";
    lastName = "";
    payRate = 15.0;
    position = "associate";
    forcePasswordChange = true;
  }

  function onLogInClick() {
    currentView.set("logIn");
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
    Pay Rate 
    <input
      type="number"
      placeholder="Pay Rate"
      value={payRate}
      on:input={(e) => {
        payRate = e.target.value;
      }}
      />
      <br />
      Position 
      <select bind:value={position}>
        <option value="associate">Associate</option>
        <option value="manager">Manager</option>
        <option value="administrator">Administrator</option>
      </select>
      <br />
      Force user to change password upon next log in 
      <input
        type="checkbox"
        bind:checked={forcePasswordChange}
        />
        <br />
    <button id="register-button" on:click={onRegisterClick}> Register </button>
  </div>
</main>

<style>
  #register-container {
    padding: 16px;
  }
</style>
