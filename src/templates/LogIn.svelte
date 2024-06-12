<script>
  // @ts-nocheck

  let email = "";
  let password = "";

  function onEmailInput(event) {
    email = event.target.value;
  }

  function onPasswordInput(event) {
    password = event.target.value;
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
  </div>
</main>

<style>
    #log-in-container {
        padding: 16px;
    }
</style>
