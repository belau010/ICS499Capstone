<script>
  import API from "../API";

  let scheduleDate = null;
  let shifts = [];

  async function onGetScheduleClick() {
    shifts = await API.shift.readByDate(scheduleDate);
  }
</script>

<main>
  <div style="display: flex; flex-direction: row">
    <div style="width: 50%; padding: 8px">
      View Full Schedule
      <hr />
      <input type="date" bind:value={scheduleDate} />
      <button on:click={onGetScheduleClick}>Get Schedule</button>
    </div>
    <div style="width: 50%; padding: 8px">
        {#each shifts as shift}
        <div style="border: 1px solid black; margin: 8px">
            {shift.workerLastName}, {shift.workerFirstName}<br /> 
            {shift.startTime} to {shift.endTime}
        </div>
        {/each}
    </div>
  </div>
</main>
