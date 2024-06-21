<script>
  import LogIn from "./templates/LogIn.svelte";
  import Register from "./templates/Register.svelte";
  let currentView = "logIn";
  const setView = (view) => {
    currentView = view;
  };
</script>

<main>
  {#if currentView === "register"}
    <Register {setView} />
  {:else if currentView === "logIn"}
    <LogIn {setView} />
  {/if}
</main>

<style>
</style>
