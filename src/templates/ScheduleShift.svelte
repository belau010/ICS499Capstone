<script>
  import API from "../API";

  let searchString = "";
  let users = [];
  let selectedUser = null;
  let startTime = null;
  let shiftLengthHrs = null;
  let shiftLengthMins = null;
  let endTime = null;
  let notes = "";

  async function onSearchClick() {
    users = await API.user.search(searchString);
  }

  function formatDateForMySQL(date) {
    const pad = (number) => number.toString().padStart(2, "0");

    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1); //Months are zero-based in JS
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());
    const seconds = pad(date.getSeconds());

    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  }

  function onCreateClick() {
    const startTimeDate = new Date(startTime);
    endTime = new Date(startTimeDate);
    endTime.setHours(endTime.getHours() + shiftLengthHrs);
    endTime.setMinutes(endTime.getMinutes() + shiftLengthMins);
    if (
      startTime !== null &&
      endTime != null &&
      selectedUser != null &&
      new Date(startTime) < new Date(endTime)
    ) {
      API.shift.create(
        selectedUser.id,
        startTime,
        formatDateForMySQL(endTime),
        notes
      );
    } else {
      alert("Invalid Entry");
    }
  }
</script>

<main>
  Schedule Shift
  <hr />
  <div style="display: flex; flex-direction: row">
    <div style="width: 50%; padding: 8px">
      <input placeholder="Search by last name..." bind:value={searchString} />
      <button on:click={onSearchClick}> Search </button>
      <hr />
      {#each users as user}
        <button
          style={user == selectedUser ? "background-color:mediumseagreen;" : ""}
          on:click={() => {
            selectedUser = user;
          }}
        >
          {user.lastName}, {user.firstName}
        </button>
        <br />
      {/each}
    </div>
    <div style="width: 50%; padding: 8px">
      Start Time: <br />
      <input
        bind:value={startTime}
        type="datetime-local"
        id="shift-starttime-input"
      /><br />
      Shift Length: <br />
      Hours:<input
        bind:value={shiftLengthHrs}
        type="number"
        id="shift-length-hrs-input"
        min="0"
        max="12"
      />
      Minutes:<input
        bind:value={shiftLengthMins}
        type="number"
        id="shift-length-mins-input"
        min="0"
        max="59"
      />
      <br />
      Notes:<br />
      <textarea bind:value={notes} style="resize: none" rows="4"></textarea>
    </div>
  </div>
  <button on:click={onCreateClick}> Schedule </button>
</main>

<style>
</style>
