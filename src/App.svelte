<script>
  import { currentView } from "./state";
  import { onMount } from "svelte";
  import Dashboard from "./templates/Dashboard.svelte";
  import LogIn from "./templates/LogIn.svelte";
  import Register from "./templates/Register.svelte";
  import ScheduleShift from "./templates/ScheduleShift.svelte";
  import API from "./API";
  import NavigationBar from "./components/NavigationBar.svelte";
  import ViewSchedule from "./templates/ViewSchedule.svelte";
  import ShiftPunch from "./templates/ShiftPunch.svelte";
  import ChangePassword from "./templates/ChangePassword.svelte";
  import UpdateUser from "./templates/UpdateUser.svelte";
  import UpdateShift from "./templates/UpdateShift.svelte";
  import ViewFullSchedule from "./templates/ViewFullSchedule.svelte";

  onMount(() => {
    API.init();
  });
</script>

<main>
  <NavigationBar />
  {#if $currentView === "register"}
    <Register />
  {:else if $currentView === "logIn"}
    <LogIn />
  {:else if $currentView === "dashboard"}
    <Dashboard />
  {:else if $currentView === "scheduleShift"}
    <ScheduleShift />
  {:else if $currentView === "viewSchedule"}
    <ViewSchedule />
  {:else if $currentView === "shiftPunch"}
    <ShiftPunch />
  {:else if $currentView === "changePassword"}
    <ChangePassword />
  {:else if $currentView === "updateUser"}
    <UpdateUser />
  {:else if $currentView === "updateShift"}
    <UpdateShift />
  {:else if $currentView === "viewFullSchedule"}
    <ViewFullSchedule />
  {/if}
</main>

<style>
</style>
