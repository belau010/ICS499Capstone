<script>
  // @ts-nocheck

  import API from "../API";

  let newPassword = "";
  let showNewPassword = false;
  let verifyNewPassword = "";
  let showVerifyNewPassword = false;

  async function onChangePasswordClick() {
    if (newPassword!=verifyNewPassword) {
        alert("Passwords must match!");
        return;
    }
    await API.user.ChangePassword(newPassword);
  }
</script>

<main>
  <input
    type={showNewPassword ? "text" : "password"}
    value={newPassword}
    on:change={(e) => {
      newPassword = e.target.value;
    }}
  />
  <button
    on:click={() => {
      showNewPassword = !showNewPassword;
    }}>{showNewPassword ? "Hide" : "Show"}</button
  >
  <br />
  <input
    type={showVerifyNewPassword ? "text" : "password"}
    value={verifyNewPassword}
    on:change={(e) => {
      verifyNewPassword = e.target.value;
    }}
  />
  <button
    on:click={() => {
      showVerifyNewPassword = !showVerifyNewPassword;
    }}>{showVerifyNewPassword ? "Hide" : "Show"}</button
  >
  <br />
  <button on:click={onChangePasswordClick}> Change Password </button>
</main>
