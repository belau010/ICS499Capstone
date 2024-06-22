<script>
  import { onMount } from "svelte";
  import Dashboard from "./templates/Dashboard.svelte";
  import LogIn from "./templates/LogIn.svelte";
  import Register from "./templates/Register.svelte";
  import axios from "axios";
  let currentView = "logIn";
  const setView = (view) => {
    currentView = view;
  };
  onMount(()=>{
    axios.defaults.withCredentials = true;
    axios.get("http://127.0.0.1:5000/user/isLoggedIn").then((response) => {
      console.log(response.data)
      if(response.data.success) {
        setView("dashboard");
      }
    });
  });
</script>

<main>
  {#if currentView === "register"}
    <Register {setView} />
  {:else if currentView === "logIn"}
    <LogIn {setView} />
  {:else if currentView === "dashboard"}
    <Dashboard />
  {/if}
</main>

<style>
</style>
