<script>
  import { onMount } from "svelte";
  import API from "../API";
  import { user } from "../state/user";
  import { get } from "svelte/store";

  let shifts = [];

  onMount(() => {
    API.shift.readByUser(get(user).id, (_shifts) => {
      shifts = _shifts;
    });
  });
</script>

<main>
  View Schedule
  <hr />
  {#each shifts as shift}
    <div style="border: 1px solid black; margin: 8px">
      <div>
        Start Time:{" " + shift.startTime}
      </div>
      <div>
        End Time:{" " + shift.endTime}
      </div>
      <div>
        Notes:{" " + shift.notes}
      </div>
    </div>
  {/each}
</main>

<style>
</style>
