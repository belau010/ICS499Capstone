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
  let shifts = [];
  let selectedShift = null;

  async function onSearchClick() {
    users = await API.user.search(searchString);
  }

  function onShiftClick(shift) {
    selectedShift = shift;
    startTime = formatDateForMyInput(new Date(shift.startTime));
    notes = shift.notes;
    const differenceInMilliseconds =
      new Date(shift.endTime).getTime() - new Date(shift.startTime).getTime();
    const differenceInMinutes = Math.floor(
      differenceInMilliseconds / 1000 / 60
    );
    shiftLengthHrs = Math.floor(differenceInMinutes / 60);
    shiftLengthMins = differenceInMinutes % 60;
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

  function formatDateForMyInput(date) {
    const pad = (n) => (n < 10 ? "0" + n : n);
    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1);
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());

    return `${year}-${month}-${day}T${hours}:${minutes}`;
  }

  function onUserSelect(user) {
    selectedUser = user;
    selectedShift = null;
    API.shift.readByUser(user.id, (_shifts) => {
      shifts = _shifts;
    });
  }

  async function onUpdateClick() {
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
      await API.shift.update(
        selectedShift.id,
        startTime,
        formatDateForMySQL(endTime),
        notes
      );
      selectedShift = null;
      shifts.length = 0;
      selectedUser = null;
    } else {
      alert("Invalid Entry");
    }
  }
</script>

<main>
  <div style="display: flex; flex-direction: row">
    <div style="width: calc(calc(100VW - 128px) / 3); padding: 8px">
      <input placeholder="Search by last name..." bind:value={searchString} />
      <button on:click={onSearchClick}> Search </button>
      <hr />
      {#each users as user}
        <button
          style={user == selectedUser ? "background-color:mediumseagreen;" : ""}
          on:click={() => {
            onUserSelect(user);
          }}
        >
          {user.lastName}, {user.firstName}
        </button>
        <br />
      {/each}
    </div>
    <div style="width: calc(calc(100VW - 128px) / 3); padding: 8px">
      Shifts
      <hr />
      {#each shifts as shift}
        <button
          style={shift == selectedShift
            ? "background-color: mediumseagreen;"
            : ""}
          on:click={() => {
            onShiftClick(shift);
          }}
        >
          {shift.startTime} to<br />
          {shift.endTime}
        </button>
        <br />
      {/each}
    </div>
    <div style="width: calc(calc(100VW - 128px) / 3); padding: 8px">
      Modify
      <hr />
      {#if selectedShift !== null}
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
        <textarea bind:value={notes} style="resize: none" rows="4"></textarea><br /><br />
        <button on:click={onUpdateClick}>Update</button>
      {/if}
    </div>
  </div>
</main>
