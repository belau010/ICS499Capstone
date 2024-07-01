<script>
  import API from "../API";
  import { currentView } from "../state";

  function onLogOutClick() {
    API.user.logOut();
  }

  function onScheduleShiftClick() {
    currentView.set("scheduleShift")
  }
</script>

<main>
  Dashboard
  <button on:click={onLogOutClick}> Log Out </button>
</main>


<style>
</style>
