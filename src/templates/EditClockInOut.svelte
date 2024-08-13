<script>
  import API from "../API";

  let searchString = "";
  let users = [];
  let selectedUser = null;
  let clocks = [];
  let selectedClock = null;
  let clockDateTime = null;

  async function onUserSelect(user) {
    selectedUser = user;
    clocks = await API.clock.readByUser(user.id);
  }

  function onClockSelect(clock) {
    selectedClock = clock;
    clockDateTime = formatDateForMyInput(new Date(clock.timeStamp));
  }

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

  function formatDateForMyInput(date) {
    const pad = (n) => (n < 10 ? "0" + n : n);
    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1);
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());

    return `${year}-${month}-${day}T${hours}:${minutes}`;
  }

  async function onUpdateClick() {
    console.log(clockDateTime)
    await API.clock.update(selectedClock.id, formatDateForMySQL(new Date(clockDateTime)));
  }
</script>

<main>
  <div style="display: flex; flex-direction: row">
    <div style="width: calc(calc(100vw - 128px) / 3); padding: 8px">
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
    <div style="width: calc(calc(100vw - 128px) / 3); padding: 8px">
      Clock Ins/Outs
      <hr />
      {#each clocks as clock}
        <button
          on:click={() => {
            onClockSelect(clock);
          }}
        >
          {clock.timeStamp}
        </button>
      {/each}
    </div>
    <div style="width: calc(calc(100vw - 128px) / 3); padding: 8px">
      Modify
      <hr />
      <input type="datetime-local" bind:value={clockDateTime} /><br />
      <button on:click={onUpdateClick}> Update </button>
    </div>
  </div>
</main>
