<script>
  import { currentView } from "../state";
  import { user } from "../state/user";

  let showMenu = true;
</script>

{#if $user !== null}
  <div id="menu-container">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div
      on:click={() => {
        showMenu = !showMenu;
      }}
    >
      Menu
    </div>
    {#if showMenu}
      <div id="menu-dropdown">
        <button
          on:click={() => {
            currentView.set("dashboard");
          }}
        >
          Home
        </button>
        <button
          on:click={() => {
            currentView.set("scheduleShift");
          }}
        >
          Schedule Shift
        </button>
        <button
          on:click={() => {
            currentView.set("viewSchedule");
          }}
        >
          View Schedule
        </button>
        <button
          on:click={() => {
            currentView.set("shiftPunch");
          }}
        >
          Clock In/Out
        </button>
      </div>
    {/if}
  </div>
{/if}

<style>
  #menu-container {
    position: fixed;
    width: 200px;
    top: 8px;
    right: 8px;
    border: 1px solid black;
  }
  #menu-dropdown {
    width: 184px;
    font-size: 24px;
    padding: 8px;
    background-color: lightskyblue;
  }
  #menu-dropdown button {
    background-color: lightskyblue;
    font-size: 16px;
  }
</style>
