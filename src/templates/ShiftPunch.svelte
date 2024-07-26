<script>
  import { onMount } from "svelte";
  import API from "../API";

  async function onShiftPunchClick() {
    await API.clock.create(isWorking);
    isWorking = !isWorking;
  }
  let isWorking = false;
  async function checkWorking() {
    isWorking = await API.clock.checkWorking();
  }
  onMount(()=>{
    checkWorking();
  });
</script>

<main>
  Shift Punch
  <hr />
  <button on:click={onShiftPunchClick}> {isWorking?"End ":"Start "}Shift
  </button>
</main>

<style>
</style>
