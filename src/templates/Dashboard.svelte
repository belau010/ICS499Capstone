<script>
  import API from "../API";

  function onLogOutClick() {
    API.user.logOut();
  }
</script>

<main>
  Dashboard
  <button on:click={onLogOutClick}> Log Out </button>
</main>

<style>
</style>
