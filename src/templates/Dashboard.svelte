<script>
  import axios from "axios";

  function onLogOutClick() {
    axios.delete("http://127.0.0.1:5000/user/logOut").then(()=>{
        window.location.href = "/"
    })
  }
</script>

<main>
  Dashboard
  <button on:click={onLogOutClick}> Log Out </button>
</main>

<style>
</style>
